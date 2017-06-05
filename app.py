from klein import Klein
from twisted.internet.address import IPv4Address, IPv6Address, UNIXAddress


class Application(object):
    app = Klein()

    @app.route('/')
    def main(self, request):
        """
        :param twisted.web.http.Request request:
        :return: User's IP
        """
        request.setHeader(b'content-type', b'text/plain')
        return str(self.get_client_ip(request))

    def get_client_ip(self, request):
        """
        :param twisted.web.server.Request request:
        :return: User's IP
        """
        client = request.client
        if isinstance(client, (IPv4Address, IPv6Address)):
            return client.host
        elif isinstance(client, (UNIXAddress,)):
            x_forwarded_for = (request.getHeader(b'x-forwarded-for') or b'').decode()
            if x_forwarded_for:
                return x_forwarded_for.split(' ')[-1]
        return 'unknown'


if __name__ == '__main__':
    txip = Application()
    txip.app.run(endpoint_description='unix:/tmp/txip.sock')

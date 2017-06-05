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
        return str(self.get_client_ip(request)) + '\n'

    def get_client_ip(self, request):
        """
        :param twisted.web.server.Request request:
        :return: User's IP
        """
        for header_name in (b'x-real-ip', b'x-forwarded-for'):
            header_value = request.getHeader(header_name)
            if header_value:
                return header_value.decode()

        client = request.client
        if isinstance(client, (IPv4Address, IPv6Address)):
            return client.host

        return 'unknown'

if __name__ == '__main__':
    txip = Application()
    txip.app.run(endpoint_description='tcp:8081')

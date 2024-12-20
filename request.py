class Request:
    def __init__(self, ip_address, method, headers, body):
        self.ip_address = ip_address
        self.method = method
        self.headers = headers
        self.body = body

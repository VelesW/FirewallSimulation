from .base_filter import Filter

class IPFilter(Filter):
    def __init__(self, whitelist, blacklist, next_filter=None):
        super().__init__(next_filter)
        self.whitelist = whitelist
        self.blacklist = blacklist

    def handle(self, request):
        if request.ip_address in self.blacklist:
            print(f"IPFilter: Blocking request from {request.ip_address} (blacklisted)")
            return False
        if request.ip_address not in self.whitelist:
            print(f"IPFilter: Blocking request from {request.ip_address} (not whitelisted)")
            return False
        print(f"IPFilter: Allowing request from {request.ip_address}")
        return super().handle(request)
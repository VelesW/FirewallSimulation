from Filters.base_filter import Filter

class IPFilter(Filter):
    def __init__(self, whitelist, blacklist, next_filter=None):
        super().__init__(next_filter)
        self.whitelist = whitelist
        self.blacklist = blacklist

    def handle(self, request):
        if request.ip_address in self.blacklist:
            return False
        if request.ip_address not in self.whitelist:
            return False
        return super().handle(request)

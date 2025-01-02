import time
from .base_filter import Filter

class RateLimitFilter(Filter):
    def __init__(self, request_limit, time_window, next_filter=None):
        super().__init__(next_filter)
        self.request_limit = request_limit
        self.time_window = time_window
        self.requests = {}

    def handle(self, request):
        now = time.time()
        if request.ip_address not in self.requests:
            self.requests[request.ip_address] = []

        # Usuwanie starych żądań
        self.requests[request.ip_address] = [
            timestamp for timestamp in self.requests[request.ip_address]
            if now - timestamp < self.time_window
        ]

        # Sprawdzanie limitu
        if len(self.requests[request.ip_address]) >= self.request_limit:
            print(f"RateLimitFilter: Blocking request from {request.ip_address} (rate limit exceeded)")
            return False

        # Dodawanie nowego żądania
        self.requests[request.ip_address].append(now)
        print(f"RateLimitFilter: Allowing request from {request.ip_address}")
        return super().handle(request)
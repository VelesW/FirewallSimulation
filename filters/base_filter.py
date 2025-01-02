class Filter:
    def __init__(self, next_filter=None):
        self.next_filter = next_filter

    def handle(self, request):
        if self.next_filter:
            return self.next_filter.handle(request)
        return True

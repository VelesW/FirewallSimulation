from .base_filter import Filter

class ContentTypeFilter(Filter):
    def __init__(self, allowed_content_types, next_filter=None):
        super().__init__(next_filter)
        self.allowed_content_types = allowed_content_types

    def handle(self, request):
        content_type = request.headers.get("Content-Type", "")
        if content_type not in self.allowed_content_types:
            print(f"ContentTypeFilter: Blocking request with Content-Type '{content_type}'")
            return False
        print(f"ContentTypeFilter: Allowing request with Content-Type '{content_type}'")
        return super().handle(request)
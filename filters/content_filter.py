from .base_filter import Filter

class ContentFilter(Filter):
    def handle(self, request):
        suspicious_patterns = ["<script>", "SELECT * FROM", "DROP TABLE"]
        for pattern in suspicious_patterns:
            if pattern in request.body:
                print(f"ContentFilter: Blocking request with body containing '{pattern}'")
                return False
        print(f"ContentFilter: Allowing request with body '{request.body[:20]}...'")
        return super().handle(request)
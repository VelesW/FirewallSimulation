from .base_filter import Filter

class ContentFilter(Filter):
    def handle(self, request):
        suspicious_patterns = ["<script>", "SELECT * FROM", "DROP TABLE"]
        for pattern in suspicious_patterns:
            if pattern in request.body:
                return False
        return super().handle(request)

from .base_filter import Filter

class HeaderFilter(Filter):
    def __init__(self, allowed_user_agents, next_filter=None):
        super().__init__(next_filter)
        self.allowed_user_agents = allowed_user_agents

    def handle(self, request):
        user_agent = request.headers.get("User-Agent", "")
        if user_agent not in self.allowed_user_agents:
            return False
        return super().handle(request)

from .base_filter import Filter
from datetime import datetime

class TimeBasedFilter(Filter):
    def __init__(self, start_hour, end_hour, next_filter=None):
        super().__init__(next_filter)
        self.start_hour = start_hour
        self.end_hour = end_hour

    def handle(self, request):
        current_hour = datetime.now().hour
        print(f"TimeBasedFilter: Current hour is {current_hour}, allowed hours are {self.start_hour} to {self.end_hour}")
        if not (self.start_hour <= current_hour < self.end_hour):
            print(f"TimeBasedFilter: Blocking request (outside allowed hours)")
            return False
        print(f"TimeBasedFilter: Allowing request (within allowed hours)")
        return super().handle(request)
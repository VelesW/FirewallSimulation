from filters.ip_filter import IPFilter
from filters.content_filter import ContentFilter
from filters.header_filter import HeaderFilter
from filters.rate_limit_filter import RateLimitFilter
from filters.time_based_filter import TimeBasedFilter
from filters.content_type_filter import ContentTypeFilter
from firewall import Firewall
from request import Request

import time
import random

# Symulacja ruchu sieciowego
def simulate_traffic(firewall):
    ip_pool = ["192.168.1.1", "192.168.1.2", "10.0.0.1", "10.0.0.2"]
    user_agents = ["Mozilla/5.0", "Chrome/90.0", "Bot/1.0"]
    content_types = ["application/json", "text/html", "application/xml"]
    bodies = [
        "Hello, world!",
        "SELECT * FROM users",
        "<script>alert('XSS')</script>",
        "DROP TABLE students",
    ]

    while True:
        # Generowanie losowego żądania
        ip = random.choice(ip_pool)
        user_agent = random.choice(user_agents)
        content_type = random.choice(content_types)
        body = random.choice(bodies)

        request = Request(ip, "POST", {"User-Agent": user_agent, "Content-Type": content_type}, body)
        print(f"Request from {ip}: User-Agent={user_agent}, Content-Type={content_type}, Body='{body[:20]}...'")
        
        # Przetwarzanie żądania przez firewall
        response = firewall.process_request(request)
        print(f"Response: {response}")
        
        # Odczekanie 2 sekund
        time.sleep(2)

# Główna funkcja
if __name__ == "__main__":
    # Tworzenie listy dozwolonych wartości
    whitelist = ["192.168.1.1", "10.0.0.1"]
    blacklist = ["192.168.1.2"]
    allowed_user_agents = ["Mozilla/5.0", "Chrome/90.0"]
    allowed_content_types = ["application/json", "text/html"]

    # Tworzenie filtrów
    ip_filter = IPFilter(whitelist, blacklist)
    content_filter = ContentFilter(ip_filter)
    header_filter = HeaderFilter(allowed_user_agents, content_filter)
    rate_limit_filter = RateLimitFilter(5, 10, header_filter)  # Max 5 żądań na 10 sekund
    time_based_filter = TimeBasedFilter(8, 18, rate_limit_filter)  # Dozwolone od 8:00 do 18:00
    content_type_filter = ContentTypeFilter(allowed_content_types, time_based_filter)

    # Konfiguracja firewall’a
    firewall = Firewall()
    firewall.configure(content_type_filter)

    # Symulacja ruchu sieciowego
    simulate_traffic(firewall)



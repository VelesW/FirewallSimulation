from filters.ip_filter import IPFilter
from filters.content_filter import ContentFilter
from filters.header_filter import HeaderFilter
from filters.rate_limit_filter import RateLimitFilter
from filters.time_based_filter import TimeBasedFilter
from filters.content_type_filter import ContentTypeFilter
from firewall import Firewall
from request import Request

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
    rate_limit_filter = RateLimitFilter(10, 60, header_filter)  # Max 10 żądań na minutę
    time_based_filter = TimeBasedFilter(8, 18, rate_limit_filter)  # Dozwolone od 8:00 do 18:00
    content_type_filter = ContentTypeFilter(allowed_content_types, time_based_filter)

    # Konfiguracja firewall’a
    firewall = Firewall()
    firewall.configure(content_type_filter)

# Przetwarzanie żądań
request1 = Request("192.168.1.1", "POST", {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}, "Hello!")
print(firewall.process_request(request1))  # Oczekiwany wynik: "200 OK"

request2 = Request("192.168.1.2", "POST", {"User-Agent": "Bot/1.0", "Content-Type": "application/json"}, "Malicious")
print(firewall.process_request(request2))  # Oczekiwany wynik: "403 Forbidden"

request3 = Request("192.168.1.1", "POST", {"User-Agent": "Mozilla/5.0", "Content-Type": "text/html"}, "SELECT * FROM users")
print(firewall.process_request(request3))  # Oczekiwany wynik: "403 OK"

# Additional requests
request4 = Request("10.0.0.1", "GET", {"User-Agent": "Chrome/90.0", "Content-Type": "application/json"}, "Fetch data")
print(firewall.process_request(request4))  # Oczekiwany wynik: "200 OK"

request5 = Request("10.0.0.1", "POST", {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}, "Submit data")
print(firewall.process_request(request5))  # Oczekiwany wynik: "200 OK"

request6 = Request("192.168.1.3", "GET", {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}, "Fetch data")
print(firewall.process_request(request6))  # Oczekiwany wynik: "403 Forbidden"  # IP not in whitelist

request7 = Request("192.168.1.1", "POST", {"User-Agent": "Mozilla/5.0", "Content-Type": "application/xml"}, "Submit data")
print(firewall.process_request(request7))  # Oczekiwany wynik: "403 Forbidden"  # Content-Type not allowed

request8 = Request("192.168.1.1", "POST", {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}, "Hello!")
print(firewall.process_request(request8))  # Oczekiwany wynik: "429 Too Many Requests"  # Rate limit exceeded


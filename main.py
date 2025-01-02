from filters import IPFilter, ContentFilter
from firewall import Firewall
from request import Request

if __name__ == "__main__":
   # Tworzenie list IP
   whitelist = ["192.168.1.1", "10.0.0.1"]
   blacklist = ["192.168.1.2"]

   # Tworzenie łańcucha filtrów
   ip_filter = IPFilter(whitelist, blacklist)
   content_filter = ContentFilter(ip_filter)

   # Konfiguracja firewall’a
   firewall = Firewall()
   firewall.configure(content_filter)

   # Przetwarzanie żądań
   request = Request("192.168.1.2", "POST", {}, "SELECT * FROM users")
   print(firewall.process_request(request))  # Oczekiwany wynik: "403 Forbidden"

   request2 = Request("10.0.0.1", "GET", {}, "Hello, world!")
   print(firewall.process_request(request2))  # Oczekiwany wynik: "200 OK"

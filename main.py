from Filters import Filter, ContentFilter, IPFilter
from firewall import Firewall
from request import Request

if __name__ == "__main__":
   # Create IP lists
   whitelist = ["192.168.1.1", "10.0.0.1"]
   blacklist = ["192.168.1.2"]

   # Chain of filters
   ip_filter = IPFilter(whitelist, blacklist)
   content_filter = ContentFilter(ip_filter)

   # Firewall config
   firewall = Firewall()
   firewall.configure(content_filter)

   # request processing
   request = Request("192.168.1.2", "POST", {}, "SELECT * FROM users")
   print(firewall.process_request(request))  # Excpected result: "403 Forbidden"

   request2 = Request("10.0.0.1", "GET", {}, "Hello, world!")
   print(firewall.process_request(request2))  # Excpected result: "200 OK"

"""
Original message from founder Randall Degges left untouched below for posterity

ipify
~~~~~

The official client library for ipify2: https://www.ipify.org - A Simple IP
Address API.

ipify will get your public IP address, and return it.  No questions asked.

ipify is a great choice because it's:

    - Open source.
    - Free to use as much as you want (*even if you want to do millions of
      requests per second*).
    - Fully distributed across Amazon's AWS cloud.
    - Got a rock-solid uptime record.
    - Personally funded by Randall Degges (http://www.rdegges.com), so it
      won't just *disappear* some day.

For more information, visit the project website: https://www.ipify.org

-Randall Degges
"""


from .ipify import get_ipv4, get_ipv6, get_universal_ip

ipify2
============

An updated unofficial clone of the now-deprecated `ipify` library, allowing you to determine your IPv4 and IPv6 programmatically via [ipify.org](https://www.ipify.org)

.. image:: https://img.shields.io/pypi/v/ipify2.svg
    :alt: ipify2 Release
    :target: https://pypi.python.org/pypi/ipify2

.. image:: https://img.shields.io/pypi/dm/ipify2.svg
    :alt: ipify2 Downloads
    :target: https://pypi.python.org/pypi/ipify2


Meta
----

### Original

- Author: Randall Degges
- Email: r@rdegges.com
- Site: http://www.rdegges.com

### Maintainer

- Author: Nate Harris
- Email: n8gr8gbln@gmail.com
- Site: https://nateharr.is


Purpose
-------

[ipify.org](https://www.ipify.org) is a reliable IP address lookup service, an easy way to get your public IP address in Python.

This library will retrieve your public IP address from ipify's API service, and return it as a string.

Additional features:

- If a request fails for any reason, it is re-attempted 3 times using an exponential backoff algorithm for maximum effectiveness.
- This library handles exceptions properly, and usage examples below show you how to deal with errors in a foolproof way.
- This library only makes API requests over HTTPS.


Installation
------------

To install ``ipify2``, simply run:

```shell
pip install ipify2
```

This will install the latest version of the library automatically.


Usage
-----

Using this library is very simple.  Here's a simple example:

```python
from ipify2 import get_ipv4

ip = get_ipv4()
print(ip) # '96.41.136.144'
```

```python
from ipify2 import get_ipv6
ip = get_ipv6()
print(ip) # '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
```

### Error Handling
There are several reasons a request fail:
- The ipify service is down
- Your machine is unable to get the request to ipify because of a network error
  of some sort (DNS, no internet, etc.).

To handle these errors, you can do the following:

```python
from ipify2 import get_universal_ip
from ipify2.exceptions import ConnectionError, ServiceError

try:
    ip = get_universal_ip()
except ConnectionError:
    # If you get here, it means you were unable to reach the ipify service,
    # most likely because of a network error on your end.
except ServiceError:
    # If you get here, it means ipify is having issues, so the request
    # couldn't be completed :(
except:
    # Something else happened (non-ipify related). Maybe you hit CTRL-C
    # while the program was running, the kernel is killing your process, or
    # something else all together.
```

If you want to simplify the above error handling by catching all errors, you could also do the following:

```python
from ipify2 import get_universal_ip
from ipify2.exceptions import IpifyException

try:
    ip = get_universal_ip()
except IpifyException:
    # If you get here, then some ipify exception occurred.
except:
    # If you get here, some non-ipify related exception occurred.
```

One thing to keep in mind: regardless of how you decide to handle exceptions,  the ipify library will retry any failed requests 3 times before ever raising exceptions -- so if you *do* need to handle exceptions, just remember that retry logic has already been attempted.

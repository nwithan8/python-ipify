"""
ipify2.ipify2
~~~~~~~~~~~

The module holds the main ipify2 library implementation.
"""


from backoff import expo, on_exception
from requests import get
from requests.exceptions import RequestException

from .exceptions import ConnectionError, ServiceError
from .settings import MAX_TRIES, USER_AGENT


@on_exception(expo, RequestException, max_tries=MAX_TRIES)
def _get_ip_resp(api_url: str):
    """
    Internal function which attempts to retrieve this machine's public IP
    address from the ipify2 service (https://www.ipify.org).

    :rtype: obj
    :returns: The response object from the HTTP request.
    :raises: RequestException if something bad happened and the request wasn't
        completed.

    .. note::
        If an error occurs when making the HTTP request, it will be retried
        using an exponential backoff algorithm.  This is a safe way to retry
        failed requests without giving up.
    """
    return get(api_url, headers={'user-agent': USER_AGENT})


def get_ipv4():
    """
    Query the ipify2 service (https://www.ipify.org) to retrieve this machine's
    public IPv4 address.

    :rtype: string
    :returns: The public IPv4 address of this machine as a string.
    :raises: ConnectionError if the request couldn't reach the ipify2 service,
        or ServiceError if there was a problem getting the IPv4 address from
        ipify2's service.
    """
    try:
        resp = _get_ip_resp(api_url="https://api.ipify.org")
    except RequestException:
        raise ConnectionError("The request failed because it wasn't able to reach the ipify2 service. This is most likely due to a networking error of some sort.")

    if resp.status_code != 200:
        raise ServiceError('Received an invalid status code from ipify2:' + str(resp.status_code) + '. The service might be experiencing issues.')

    return resp.text


def get_universal_ip():
    """
    Query the ipify2 service (https://www.ipify.org) to retrieve this machine's
    public IPv4/IPv6 address.

    :rtype: string
    :returns: The public IPv4/IPv6 address of this machine as a string.
    :raises: ConnectionError if the request couldn't reach the ipify2 service,
        or ServiceError if there was a problem getting the IPv4/IPv6 address from
        ipify2's service.
    """
    try:
        resp = _get_ip_resp(api_url="https://api64.ipify.org")
    except RequestException:
        raise ConnectionError("The request failed because it wasn't able to reach the ipify2 service. This is most likely due to a networking error of some sort.")

    if resp.status_code != 200:
        raise ServiceError('Received an invalid status code from ipify2:' + str(resp.status_code) + '. The service might be experiencing issues.')

    return resp.text

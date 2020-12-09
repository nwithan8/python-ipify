"""
ipify2.settings
~~~~~~~~~~~~~~

This module contains internal settings that make our ipify2 library simpler.
"""


from platform import mac_ver, win32_ver, system, platform
from sys import version_info as vi

from .__info__ import __version__

# The maximum amount of tries to attempt when making API calls.
MAX_TRIES = 3

# This dictionary is used to dynamically select the appropriate platform for
# the user agent string.
OS_VERSION_INFO = {
    'Linux': '%s' % (platform()),
    'Windows': '%s' % (win32_ver()[0]),
    'Darwin': '%s' % (mac_ver()[0]),
}

# The user-agent string is provided so that I can (eventually) keep track of
# what libraries to support over time.  EG: Maybe the service is used primarily
# by Windows developers, and I should invest more time in improving those
# integrations.
USER_AGENT = 'python-ipify2/%s python/%s %s/%s' % (
    __version__,
    '%s.%s.%s' % (vi.major, vi.minor, vi.micro),
    system(),
    OS_VERSION_INFO.get(system(), ''),
)

"""
setup.py
~~~~~~~~

Packaging information and tools.
"""

from subprocess import call
from sys import exit

from setuptools import Command, setup

import ipify2.__info__ as package_info

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", 'r') as fh:
    requirements = fh.read().splitlines()


class TestCommand(Command):
    """
    The ``python setup.py test`` command line invocation is powered by this
    helper class.

    This class will run ``py.test`` behind the scenes and handle all command
    line arguments for ``py.test`` as well.
    """
    description = 'run all tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run the test suite."""
        exit(call(['py.test', '--cov-report', 'term-missing', '--cov', 'ipify2']))


setup(
    name=package_info.__title__,  # How you named your package folder (MyLib)
    packages=[package_info.__title__],  # Choose the same as "name"
    version=package_info.__version__,  # Start with a small number and increase it with every change you make
    license=package_info.__license__,
    description="Get IP address information via ipify.org",  # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=package_info.__author__,  # Type in your name
    author_email=package_info.__author_email__,  # Type in your E-Mail
    url=f'https://github.com/nwithan8/{package_info.__title__}',
    download_url=f'https://github.com/nwithan8/{package_info.__title__}/archive/{package_info.__version__}.tar.gz',
    # Package dependencies:
    install_requires=requirements,
    tests_require=requirements,
    # Test harness:
    cmdclass={
        'test': TestCommand,
    },
    keywords=['Python', 'API', 'client', 'ipify', 'ipify2', 'ip', 'address', 'public', 'ipv4', 'ipv6', 'service'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    python_requires='>=3.0'
)

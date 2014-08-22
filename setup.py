from distutils.core import setup, Extension

nmap = Extension('nmap',
                 sources = ['nmap/nmap.py', 'nmap/__init__.py', 'nmap/example.py'])
from nmap import *

# Install : python setup.py install
# Register : python setup.py register

#  platform = 'Unix',
#  download_url = 'https://github.com/sleach/python-nmap',


setup (
    name = 'python-nmap',
    version = nmap.__version__,
    author = 'Alexandre Norman',
    author_email = 'norman@xael.org',
    license ='LICENSE'
    keywords="nmap, portscanner, network, sysadmin",
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    platforms=[
        "Operating System :: OS Independent",
        ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
                                    "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: System :: Networking :: Monitoring",
        ],
    packages=['nmap'],
    url = 'https://github.com/sleach/python-nmap',
    description = 'This is a python class to use nmap and access scan results from python',
    long_description=open('README.md').read() + "\n" + open('CHANGELOG').read(),
)

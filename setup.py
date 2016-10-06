try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION="0.1.0"

config = {
	'name':'rosetta_sip_factory',
	'version':VERSION,
	'author':'Sean Mosely',
	'author_email':'sean.mosely@gmail.com',
	'packages':['rosetta_sip_factory',],
	'description':'Python library for building Submission Information Packages for the Rosetta digital preservation application',
	'install_requires':['lxml==3.6.4',],
	'download_url': 'https://github.com/NLNZDigitalPreservation/rosetta_sip_factory/archive/v'+VERSION+'.tar.gz',
	'license': 'MIT'
	}

setup(**config)
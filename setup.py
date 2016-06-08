#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import sys
import logging

from armoryutxsvr import config

required_packages = [
    'flask==0.11.1',
    'json-rpc==1.10.3',
    'pytest==2.9.2',
    'requests==2.10.0'
]

setup_options = {
    'name': 'armory-utxsvr',
    'version': config.VERSION,
    'author': 'Counterparty Developers',
    'author_email': 'support@counterparty.io',
    'maintainer': 'Counteparty Developers',
    'maintainer_email': 'dev@counterparty.io',
    'url': 'http://counterparty.io',
    'license': 'MIT',
    'description': 'armory UTXsvr',
    'long_description': 'Provides a JSON RPC interface to armory for production and signing of offline transactions',
    'keywords': 'counterparty, bitcoin, armory, armory-utxsvr',
    'classifiers': [
      "Programming Language :: Python",
    ],
    'download_url': 'https://github.com/CounterpartyXCP/armory-utxsvr/releases/tag/%s' % config.VERSION,
    'provides': ['armoryutxsvr'],
    'packages': find_packages(),
    'zip_safe': False,
    'install_requires': required_packages,
    'include_package_data': True,
    'entry_points': {
        'console_scripts': [
            'armory-utxsvr = armoryutxsvr:server_main',
        ]
    },
}

if os.name == "nt":
    sys.exit("Windows installs not supported")

setup(**setup_options)

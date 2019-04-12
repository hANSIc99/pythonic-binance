#!/usr/bin/env python
from setuptools import setup

setup(
    name='pythonic_binance',
    version='0.7.1',
    packages=['pythonic_binance'],
    description='Binance REST API python implementation',
    url='https://github.com/hANSIc99/pythonic-binance',
    author='Sam McHardy',
    #package_dir = {'' : 'pythonic_binance'},
    license='MIT',
    author_email='',
    install_requires=['requests' ],
    keywords='exchange rest api bitcoin ethereum btc eth neo',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

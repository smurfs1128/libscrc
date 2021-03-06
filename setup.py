# -*- coding:utf-8 -*-
""" Setup script for CRC8/CRC16/CRC32/CRC64 library. """
from os import path
from setuptools import setup, find_packages, Extension
from codecs import open

# !/usr/bin/python
# Python:   3.5.2+
# Platform: Windows/Linux/MacOS/ARMv7
# Author:   Heyn (heyunhuan@gmail.com)
# Program:  Library CRC8/CRC16/CRC32/CRC64 Modules.
# History:  2017-08-09 Wheel Ver:0.0.1 [Heyn] Initialize
#           2017-08-10 Wheel Ver:0.0.2 [Heyn] New add CRC8 (IntelHex/BCC/LRC/CRC8(VERB))
#           2017-08-17 Wheel Ver:0.0.3 [Heyn] Optimized Code.
#                      Wheel Ver:0.0.4 [Heyn] New CRC16-SICK / CRC16-DNP.
#           2017-08-17 Wheel Ver:0.0.5 [Heyn] New CRC64-ISO / CRC64-ECMA182.
#           2017-08-22 Wheel Ver:0.1.2 [Heyn] Optimization code for the C99 standard.
#           2017-09-19 Wheel Ver:0.1.3 [Heyn] New CRC16-X25.
#           2020-03-17 Wheel Ver:1.0   [Heyn] New hacker16 / hacker32 / hacker64

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
    long_description = long_description.replace("\r", "")

setup(
    name='libscrc',
    version='1.0',

    description='Library for calculating CRC4/CRC8/CRC16/CRC32/CRC64',
    long_description=long_description,

    url='https://github.com/hex-in/libscrc',

    author='Heyn',
    author_email='heyunhuan@gmail.com',

    license='MIT',

    platforms='any',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    keywords=['CRC4', 'CRC5', 'CRC6', 'CRC7', 'CRC8', 'CRC16', 'CRC32', 'CRC64'],

    packages=['libscrc'],

    include_package_data=True,

    ext_modules=[Extension('libscrc._crcx',  sources=['src/crcx/_crcxmodule.c',   'src/crcx/_crcxtables.c'  ]),
                 Extension('libscrc._crc8',  sources=['src/crc8/_crc8module.c',   'src/crc8/_crc8tables.c'  ]),
                 Extension('libscrc._crc16', sources=['src/crc16/_crc16module.c', 'src/crc16/_crc16tables.c']),
                 Extension('libscrc._crc32', sources=['src/crc32/_crc32module.c', 'src/crc32/_crc32tables.c']),
                 Extension('libscrc._crc64', sources=['src/crc64/_crc64module.c', 'src/crc64/_crc64tables.c']),
                ],
)

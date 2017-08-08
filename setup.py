#!/usr/bin/env python

from setuptools import setup


setup(name='testpackage',
    version='0.0.1',
    description='Test package for travis',
    long_description='Some sort of test package for playing around with',
    author='Necross',
    author_email='blabla@blabla.com',
    url='',
    packages=[
    'testpackage',
    'testpackage.package',
    ],
    package_data={'': ['LICENSE.txt']},
    install_requires=[
        'six==1.10.0'
    ],
    classifiers=[
          'Development Status :: 1 - Beta',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering',
          'Topic :: Software Development'
          ],
    license='BSD'
)

#!/usr/bin/env python
import io
from setuptools import find_packages, setup


readme = io.open('README.rst', 'r', encoding='utf-8').read()


setup(
    name='aratrum',
    description='A simple configuration handler',
    long_description=readme,
    url='https://github.com/Vesuvium/aratrum',
    author='Jacopo Cascioli',
    author_email='jacopocascioli@gmail.com',
    license='MIT',
    version='0.0.1',
    packages=find_packages(),
    tests_require=[
        'pytest',
        'pytest-mock'
    ],
    setup_requires=['pytest-runner'],
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)

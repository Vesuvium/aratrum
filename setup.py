#!/usr/bin/env python
import io

from setuptools import find_packages, setup


readme = io.open('README.rst', 'r', encoding='utf-8').read()


setup(
    name='aratrum',
    description='A simple json configuration handler.',
    long_description=readme,
    url='https://github.com/Vesuvium/aratrum',
    author='Jacopo Cascioli',
    author_email='jacopocascioli@gmail.com',
    license='MIT',
    version='0.3.2',
    packages=find_packages(),
    tests_require=[
        'pytest',
        'pytest-mock'
    ],
    setup_requires=['pytest-runner'],
    install_requires=[
        'ujson>=1.35'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ]
)

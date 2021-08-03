# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="test",
    version="1.0",
    author="libin",
    author_email="",
    description=("test项目"),
    platforms='python3',
    packages=find_packages(),
    install_requires=[
        'pymssql',
        #'requests',
        #'DBUtils',
        #'cx_Oracle',
        #'python-dateutil'
    ]
)

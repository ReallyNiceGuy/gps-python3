import os
from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

install_reqs = parse_requirements("requirements.txt", session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name = "gpspy3",
    version = "0.1.0",
    packages=find_packages(),
    author = "",
    author_email = "",
    description = (""),
    license = "",
    keywords = "",
    url = "",
    install_requires=reqs
)


from os.path import abspath, dirname, join
from setuptools import find_packages, setup  # type: ignore


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name="clmv2-opensearch-client",
    version="1.0.11",
    url="https://git.autodesk.com/IBP/clmv2-opensearch-client.git",
    author="CLMv2 Team - Daedalus",
    description="Client to manage data stored in opensearch(AWS)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests",
        "opensearch-py==2.2.0",
    ],
)
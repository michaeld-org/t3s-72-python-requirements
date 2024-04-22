from os.path import abspath, dirname, join

from setuptools import find_packages, setup  # type: ignore

with open(join(dirname(abspath(__file__)), "README.md")) as readme_file:
    README_MD = readme_file.read()
    
#if __name__ == "__main__":
setup(
    name="clmv2-opensearch-client",
    version="1.0.12",  # PEP-440 (e.g. 1.2.dev1, 1.1a1 etc)
    url="https://git.autodesk.com/IBP/clmv2-opensearch-client.git",
    author="CLMv2 Team - Daedalus",
    packages=find_packages(),
    description="Client to manage data stored in opensearch(AWS)",
    long_description_content_type="text/markdown",
    install_requires=[
        "requests",
        "opensearch-py==2.2.0",
    ],
)

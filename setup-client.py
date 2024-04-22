from os.path import abspath, dirname, join

from setuptools import find_packages, setup  # type: ignore

README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

if __name__ == "__main__":
    setup(
        name="clmv2-opensearch-client",
        version="1.0.11",  # PEP-440 (e.g. 1.2.dev1, 1.1a1 etc)
        url="https://git.autodesk.com/IBP/clmv2-opensearch-client.git",
        author="CLMv2 Team - Daedalus",
        description="Client to manage data stored in opensearch(AWS)",
        long_description=README_MD,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=[
            # Do not restrict requests version to avoid conflicting
            # dependancies on other projects
            "requests",
            "opensearch-py==2.2.0",
        ],
    )

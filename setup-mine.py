from setuptools import setup, find_packages

setup(
    name='ExamplePackage',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',  # An example of a third-party package as a dependency
    ],
    python_requires='>=3.6',
    author='Michael',
    author_email='michael.dahis@snyk.io',
    description='A simple example package',
    license='MIT',
)

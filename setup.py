from setuptools import setup, find_packages

# This is a fork of https://github.com/marcjulianschwarz/watchlib

setup(
    name='watchlib',
    version='1.0.0',
    packages=find_packages(),
    license='MIT',
    classifiers=[],
    install_requires=open('requirements.txt').read().splitlines(),
)


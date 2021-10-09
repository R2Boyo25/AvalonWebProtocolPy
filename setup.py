
from setuptools import find_packages, setup

setup(
    name='AWP',
    packages=find_packages(include=['AWP']),
    version='0.3',
    description='AvalonWebProtocol',
    author='R2Boyo25',
    license='GPLV3',
    install_requires=['lz4']
)
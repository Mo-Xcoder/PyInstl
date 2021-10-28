from setuptools import find_packages, find_namespace_packages
from setuptools import setup

setup(
    name="PyInstl",
    version='1.0.1',
    description='A package installer cli for python',
    author='Muhammed Mehmood',
    author_email='ifreezeu2@gmail.com',
    url='https://github.com/Mo-Xcoder/PyInstl',
    install_requires=[
        "argparse",
        "subprocess",
        "pyfiglet",
        "clint"
    ],
    packages=find_namespace_packages(include=['PyInstl.*']),
    entry_points={
        'console_scripts': [
            'PyInstl = PyInstl.main:main',
        ],
    },
)
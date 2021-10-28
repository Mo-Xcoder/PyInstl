from setuptools import find_packages
from setuptools import setup

setup(
    name="PyInstl",
    version='1.0.0',
    description='A package installer cli for python',
    author='Muhammed Mehmood',
    author_email='ifreezeu2@gmail.com',
    url='https://github.com/Mo-Xcoder/PyInstl',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'PyInstl = PyInstl.main:main',
        ],
    },
)
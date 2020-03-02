"""
conda environment automation deployment
"""

__author__ = 'liyc'
__date__ = '2020/02/27'

from setuptools import setup, find_packages

setup(
    name="CEAD",
    version="1.1",
    url="https://github.com/g-lyc/CEAD",
    description=__doc__.strip('\n'),
    license="liyc",
    author="liyc",
    author_email="liyichen2015@gmail.com",
    packages=find_packages(),
    install_requires=['docopt', 'conda-pack'],
    entry_points={
        "console_scripts": ["CEAD = CEAD:main"]
        },
)


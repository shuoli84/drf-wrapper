import setuptools
from distutils.core import setup

setup(
    name="drf_wrapper",
    author="lishuo",
    author_email="shuoli84@gmail.com",
    url="https://github.com/shuoli84/drf-wrapper",
    version="0.1",
    packages=['drf_wrapper'],
    install_requires=[
        'Django', 'djangorestframework'
    ],
    license='MIT',
    long_description=open('README.txt').read()
)

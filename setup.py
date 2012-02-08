from os.path import dirname, join
from setuptools import setup, find_packages

from contacts import get_version


def fread(fn):
    with open(join(dirname(__file__), fn), 'r') as f:
        return f.read()

setup(
    author = 'George Hickman',
    author_email = 'dev@incuna.com',
    description = 'Provide a way to push a list of contacts to phone handsets via their base station.',
    install_requires = ('django-extensible-profiles>=0.6', 'vobject>=0.8.1c',),
    long_description = fread('README.md'),
    name = 'contacts',
    packages = find_packages(),
    url = 'http://github.com/incuna/incuna-contacts',
    version = get_version(),
)


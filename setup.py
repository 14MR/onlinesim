import setuptools
from distutils.core import setup

setup(

    name = 'onlinesim',
    packages = ['onlinesim'],
    version = '0.1.0',
    license = 'MIT',
    description = 'Wrapper for onlinesim.ru service.',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    author = 'retxxxirt',
    author_email = 'retxxirt@gmail.com',
    url = 'https://github.com/retxxxirt/onlinesim',
    keywords = ['onlinesim', 'onlinesim.ru', 'online sim',
                'online sms', 'receive sms', 'sms receiver', 'receive sms online'],
    install_requires = ['requests', 'wheel']
)

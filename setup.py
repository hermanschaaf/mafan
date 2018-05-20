from setuptools import setup
from distutils.core import Command
import os
import sys
import codecs


class TestCommand(Command):
    description = "Run tests"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        errno = subprocess.call(['nosetests', '--debug=DEBUG', '-s'])
        raise SystemExit(errno)

setup(
    name='mafan',
    version='0.3.1',
    author='Herman Schaaf',
    author_email='herman@ironzebra.com',
    packages=[
        'mafan',
        'mafan.hanzidentifier',
        'mafan.third_party',
        'mafan.third_party.jianfan'
    ],
    scripts=['bin/convert.py'],
    url='https://github.com/hermanschaaf/mafan',
    license='LICENSE.txt',
    description='A toolbox for working with the Chinese language in Python',
    long_description=codecs.open('docs/README.md', 'r', 'utf-8').read(),
    cmdclass={
        'test': TestCommand,
    },
    install_requires=[
        "jieba == 0.37",
        "argparse == 1.1",
        "chardet >= 2.1.1",
        "future",
    ],
)

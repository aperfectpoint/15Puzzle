from setuptools import setup
from setuptools.command.test import test as TestCommand
import io
import os
import sys

import puzzle15

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.md')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='15puzzle',
    version=puzzle15.__version__,
    url='https://github.com/aperfectpoint/15Puzzle/',
    license='Apache Software License',
    author='Amir Kafri',
    tests_require=['pytest'],
    install_requires=[],
    cmdclass={'test': PyTest},
    author_email='kafri.amir@gmail.com',
    description='A terminal-based Puzzle 15',
    long_description=long_description,
    packages=['puzzle15'],
    include_package_data=True,
    platforms='any',
    test_suite='puzzle15.test.test_2x2_board',
    classifiers=[
        'Programming Language :: Python'
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
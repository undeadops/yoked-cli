
import re
import os
from setuptools import setup
from yokedclient import __version__

version = __version__

if not version:
    raise RuntimeError('Cannot find version information')

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

with open('requirements/common.txt') as f:
    requirements = [r.strip() for r in f.readlines()]

with open('requirements/test.txt') as f:
    test_requirements = [r.strip() for r in f.readlines()]

setup(name='yoked-client',
      version=version,
      description='SSH Key Managment Configuration Tool',
      long_description=long_descr,
      url='https://github.com/metarx/yoked',
      author='Mitch Anderson',
      author_email='mitch@metauser.net',
      license='MIT',
      packages=['yokedclient'],
      zip_safe=False,
      install_requires=requirements,
      entry_points = {
          'console_scripts': ['yokedctl = yokedclient.cli:main'],
          },
      setup_requires=["pytest-runner"],
      tests_require=test_requirements
      )

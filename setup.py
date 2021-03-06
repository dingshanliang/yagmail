from setuptools import setup
from setuptools import find_packages

MAJOR_VERSION = '0'
MINOR_VERSION = '8'
MICRO_VERSION = '172'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'tests/run_tests.py'])
        raise SystemExit(errno)


setup(name='yagmail',
      version=VERSION,
      description='Yet Another GMAIL client',
      url='https://github.com/kootenpv/yagmail',
      author='Pascal van Kooten',
      author_email='kootenpv@gmail.com',
      license='MIT',
      extras_require={
          "all": ["keyring"]
      },
      keywords='email mime automatic html attachment',
      entry_points={
          'console_scripts': ['yagmail = yagmail.__main__:main']
      },
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Customer Service',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: Microsoft',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Communications :: Email',
          'Topic :: Communications :: Email :: Email Clients (MUA)',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Debuggers',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Software Distribution',
          'Topic :: System :: Systems Administration',
          'Topic :: Utilities'
      ],
      packages=find_packages(),
      zip_safe=False,
      platforms='any')

from setuptools import find_packages, setup
import os
import re


READMEFILE = 'README.rst'
VERSIONFILE = os.path.join('fredrik', '__init__.py')
VSRE = r"""^__version__ = ['"]([^'"]*)['"]"""


def get_version():
    verstrline = open(VERSIONFILE, 'rt').read()
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        return mo.group(1)

    raise RuntimeError(
        'Unable to find version string in {0}.'.format(VERSIONFILE))


setup(
    name='fredrik',
    version=get_version(),
    author='Will Kahn-Greene',
    author_email='willg@bluesock.org',
    description='Flask project template for hack-day suitable apps',
    long_description=open(READMEFILE).read(),
    url='https://github.com/willkg/fredrik',
    license='BSD 3-clause',
    zip_safe=False,
    scripts=["bin/fredrik-cmd"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ]
)

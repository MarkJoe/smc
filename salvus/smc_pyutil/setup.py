"""
WARNING: This module assumes you have *Sage* installed -- http://sagemath.org -- and are using its Python.

To run the (probably still miniscule) unit tests:

    sage -python setup.py test

You can install locally:

    sage -pip install --upgrade --user ./

"""
def readme():
    with open('README.md') as f:
        return f.read()

from setuptools import setup

setup(
    name             = 'smc_pyutil',
    version          = '1.0',
    description      = 'SageMathCloud Python Utilities',
    long_description = readme(),
    url              = 'https://github.com/sagemathinc/smc',
    author           = 'SageMath, Inc.',
    author_email     = 'office@sagemath.com',
    license          = 'GPLv3+',
    packages         = ['smc_pyutil'],
    install_requires = ['markdown2'],
    zip_safe        = False,
    classifiers     = [
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python :: 2.7',
        'Topic :: Mathematics :: Server',
    ],
    keywords        = 'server mathematics cloud',
    scripts         = ['smc_pyutil/bin/sage_server'],
    entry_points    = {
        'console_scripts': [
            'sagews2pdf           = smc_pyutil.sagews2pdf:main',
            'sws2sagews           = smc_pyutil.sws2sagews:main',
            'docx2txt             = smc_pyutil.docx2txt:main',
            'smc-open             = smc_pyutil.smc_open:main',
            'open                 = smc_pyutil.smc_open:main',
            'smc-new-file         = smc_pyutil.new_file:main',
            'smc-state            = smc_pyutil.status:main',
            'smc-ipython-notebook = smc_pyutil.ipython_notebook:main'
        ]
    },
    include_package_data = True
)
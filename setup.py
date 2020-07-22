# Copyright (C) 2020 Samuel Baker

DESCRIPTION = "Simple Objected based approach to using data from a csv"
LONG_DESCRIPTION = """
# csvObject

Simple Objected based approach to using data from a csv

<!--ABOUT THE PROJECT -->

## About The Project

csvObject is just a simple object base approach to loading in a csv file and using the data. In more complex cases when
doing actual data analysis or changing the structure of the file, using [pandas](https://github.com/pandas-dev/pandas)
makes much more sense. But if all you want is to have a light weight way of extracting the data from the csv file parsed
into an object with a few basic options without Numpy then this may be of interest.

All the source code can be found at the [csvObject git repository](https://github.com/sbaker-dev/csvObject) with 
additional information found on the [docs site](https://sbaker-dev.github.io/csvObject/)

"""
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

DISTNAME = 'csvObject'
MAINTAINER = 'Samuel Baker'
MAINTAINER_EMAIL = 'samuelbaker.researcher@gmail.com'
LICENSE = 'MIT'
DOWNLOAD_URL = "https://github.com/sbaker-dev/csvObject"
VERSION = "0.03.2"
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [

]

PACKAGES = [
    "csvObject",
]

CLASSIFIERS = [
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

if __name__ == "__main__":

    from setuptools import setup

    import sys

    if sys.version_info[:2] < (3, 7):
        raise RuntimeError("csvObject requires python >= 3.7.")

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
        license=LICENSE,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        classifiers=CLASSIFIERS
    )

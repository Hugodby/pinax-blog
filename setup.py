from setuptools import find_packages, setup

LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-blog.svg
    :target: https://pypi.python.org/pypi/pinax-blog/

==========
Pinax Blog
==========

.. image:: https://img.shields.io/pypi/v/pinax-blog.svg
    :target: https://pypi.python.org/pypi/pinax-blog/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/pinax-blog/

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-blog.svg
    :target: https://circleci.com/gh/pinax/pinax-blog
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-blog.svg
    :target: https://codecov.io/gh/pinax/pinax-blog
.. image:: https://img.shields.io/github/contributors/pinax/pinax-blog.svg
    :target: https://github.com/pinax/pinax-blog/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-blog.svg
    :target: https://github.com/pinax/pinax-blog/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-blog.svg
    :target: https://github.com/pinax/pinax-blog/pulls?q=is%3Apr+is%3Aclosed

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/

``pinax-blog`` is a blog app for Django.

Features
--------

* support for multiple channels (e.g. technical vs business)
* use of Creole (optional) and Markdown as markup format
* Atom and RSS feeds
* previewing of blog posts before publishing
* optional ability to announce new posts on twitter
* Traditional date based urls or simpler slug-only urls, via configuration
* Control over opengraph and twitter card meta data per post
* Review comments per post for multi-author workflows
* public but secret urls for unpublished blog posts for easier review

Supported Django and Python Versions
------------------------------------

* Django 1.8, 1.10, 1.11, and 2.0
* Python 2.7, 3.4, 3.5, and 3.6
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxprojects.com",
    description="Blogging app for the Django web framework",
    name="pinax-blog",
    long_description=LONG_DESCRIPTION,
    version="6.3.1",
    url="http://github.com/pinax/pinax-blog/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "pinax.blog": [
            "templates/pinax/blog/*.xml",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django>=1.8",
        "django-appconf>=1.0.1",
        "pytz>=2016.6.1",
        "Pillow>=3.0.0",
        "Markdown>=2.6.5",
        "Pygments>=2.0.2",
        "pinax-images>=2.1.0",
    ],
    tests_require=[
        "pinax-theme-bootstrap>=7.4.0",
    ],
    test_suite="runtests.runtests",
    zip_safe=False
)

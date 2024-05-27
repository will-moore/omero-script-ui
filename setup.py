#!/usr/bin/env python
#
# Copyright (c) 2024 University of Dundee.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
from setuptools import setup, find_packages

url = "https://github.com/will-moore/omero-script-ui"
version = "0.1.0.dev0"

setup(
    name="omero-script-ui",
    version=version,
    description="Experimental app to add custom UIs for OMERO scripts",
    packages=find_packages(),
    keywords=["omero"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Affero General Public License v3 ",  # noqa
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],  # Get strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    author="Will Moore",
    author_email="w.moore@dundee.ac.uk",
    license="AGPLv3",
    url="%s" % url,
    zip_safe=False,
    download_url="%s/v%s.tar.gz" % (url, version),
    include_package_data=True,
)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: 2023-02-16 21:28:46
# Author: WenWei
# -----
# Last Modified: 2023-02-20 13:00:06
# Modified By: WenWei
# -----
# Copyright (c) 2023 WenWei.
# 
# -----
# HISTORY:
# Date    /tBy	Comments
# ----------	---	----------------------------------------------------------
###
import setuptools

__VERSION__ = "0.0.2"

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "PrinterSDK",
    version = __VERSION__,
    author = "NikZ",
    author_email = "nicholas_zww@yahoo.com",
    description = "This a python SDK package for Honeywell Fiji printers",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/nicholas-zww/PrinterSDK",
    project_urls = {
        "Source" : "https://github.com/nicholas-zww/PrinterSDK",
        "Bug Tracker": "https://github.com/nicholas-zww/PrinterSDK/issues",
        "Documentation": "https://github.com/nicholas-zww/PrinterSDK/docs",
    },
    classifiers = [
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir = {"": "PrinterSDK"},
    packages = setuptools.find_packages(where="PrinterSDK"),
    python_requires = ">=3.6",
)

# -*- coding: UTF−8 -*-

import os

from setuptools import setup, find_packages

from tlv_play.main.helper.constants_config import ConfigConst

# all packages dependencies
packages = find_packages()
if not packages:
    print(f'Selecting Hardcoded Packages')
    packages = [
        "tlv_play",
    ]
print(f'Packages are {packages}')
# potential dependencies
install_reqs = [
]

# get long description from the README.md
with open(os.path.join(os.path.dirname(__file__), "README.md"), "r", encoding="utf-8") as fd:
    long_description = fd.read()

setup(
    name=ConfigConst.TOOL_NAME,
    version=ConfigConst.TOOL_VERSION_DETAILED,
    author="Pratik Jaiswal",
    author_email="impratikjaiswal@gmail.com",
    description="Generic TLV Parser.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/impratikjaiswal/tlvPlay",
    project_urls={
        "Bug Tracker": "https://github.com/impratikjaiswal/tlvPlay",
    },
    keywords="TLV Parser Tag Length Value",
    license="MIT",
    python_requires=">=3.9",
    packages=packages,
    install_requires=install_reqs
    # test_suite="test.sample_package",
)

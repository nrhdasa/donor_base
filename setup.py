from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in donor_base/__init__.py
from donor_base import __version__ as version

setup(
	name="donor_base",
	version=version,
	description="Ahmedabad Temple Donor Base Management",
	author="Narahari Dasa",
	author_email="nrhdasa@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

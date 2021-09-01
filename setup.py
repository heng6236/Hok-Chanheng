from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in form_course_register/__init__.py
from form_course_register import __version__ as version

setup(
	name="form_course_register",
	version=version,
	description="Form Course Register",
	author="Z1",
	author_email="infor@flexible.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

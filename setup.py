from setuptools import setup, find_packages

setup(
	name = "pycloser",
	version = "0.2",
	packages = find_packages(),
	author = "Arvin Kulagin",
	author_email = "arvinkulagin@yandex.ru",
	description = "Сlean exit for Python scripts after Ctrl-C.",
	long_description = open("README.rst").read(),
	license = "MIT",
	keywords = "signals exit",
	url = "https://github.com/arvinkulagin/pycloser"
)
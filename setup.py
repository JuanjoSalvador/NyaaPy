from os import path

from setuptools import find_packages, setup  # type: ignore

currdir = path.abspath(path.dirname(__file__))
with open(path.join(currdir, "README.md"), encoding="utf-8") as f:
    long_desc = f.read()

setup(
    name="nyaapy",
    version="0.6.3",
    install_requires=[
        "requests",
        "lxml",
        "aiohttp",
        "uvloop"
    ],
    url="https://github.com/juanjosalvador/nyaapy",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    download_url=("https://github.com/juanjosalvador/" "nyaapy/archive/0.6.3.tar.gz"),
    license="MIT",
    author="Juanjo Salvador",
    author_email="juanjosalvador@netc.eu",
    description="Allows you to make requests on Nyaa.si and nyaa.pantsu.cat",
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
)

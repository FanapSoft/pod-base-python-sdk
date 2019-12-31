import setuptools
from setuptools import setup
from pod_base import __version__
from os import path

here = path.abspath(path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pod-base",
    version=__version__,
    url="https://github.com/FanapSoft/pod-base-python-sdk",
    license="MIT",
    author="ReZa ZaRe",
    author_email="rz.zare@gmail.com",
    description="Base package for implementation of POD platform APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["pod", "pod sdk"],
    packages=setuptools.find_packages(exclude=("build", "dist")),
    install_requires=[
        "requests>=2.22",
        "jsonschema>=3.2"
    ],
    classifiers=[
        "Natural Language :: English",
        "Natural Language :: Persian",
    ],
    python_requires='>=2.7',
    package_data={
        'pod_base': ['*.ini']
    },
    project_urls={
        'Documentation': 'http://docs.pod.ir/v1.0.0.2/PODSDKs/python/5200/prerequisite',
        'Source': 'https://github.com/FanapSoft/pod-base-python-sdk',
        'Tracker': 'https://github.com/FanapSoft/pod-base-python-sdk/issues',
    }
)

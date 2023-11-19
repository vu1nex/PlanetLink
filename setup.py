# encoding: utf-8
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="PlanetLink",
    version="0.0.2",
    author="vu1nex",
    author_email="me@vu1nex.com",
    description="A pypi package to send message in different mediums.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vu1nex/PlanetLink",
    keywords=['wx', 'wechat', 'bot', 'message', 'reminder'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
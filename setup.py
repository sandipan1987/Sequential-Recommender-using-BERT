import os

from setuptools import setup

path = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(path, "requirements.txt"), encoding="utf-8") as f:
        REQUIRED = f.read().split("\n")
except FileNotFoundError:
    REQUIRED = []

setup(
    name="BERT4Rec",
    version="0.0.1",
    author="Sandipan Nag",
    author_email="nag.sandipan@gmail.com",
    description="BERT4Rec Sequential Recommender",
    license="MIT",
    keywords="recommender",
    url="",
    packages=["recommender"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=REQUIRED,
)
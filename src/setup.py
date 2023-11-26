import setuptools
import os
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dremo-awesomecalculator", # Replace with your own username
    version= "1.0.0",
    author="Michael",
    author_email="dedreira@github.com",
    description="An awesome calculator packagee",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dedreira/awesomecalculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approve :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
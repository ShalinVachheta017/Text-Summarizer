'''

This file is part of Text-Summerizer.

This file contains the setup.py configuration for the Text-Summerizer project.

The setup.py file is used to create a Python package for the Text-Summerizer project. 
It includes metadata such as name, version, author, email, license, URL, and project URLs. 
It also specifies the package directory and packages to be included in the distribution.

The long_description field is set to read the contents of the README.md file. 
The README.md file contains a detailed description of the project.

The setup.py file is then executed using the setuptools module, 
which generates the Python package distribution.

The generated Python package distribution can be installed using pip by running:

pip install -e 

'''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPONAME = "Text-Summerizer"
AUTHOR_USER_NAME = "shalinvachheta017"
SRC_REPO = "textSummerizer"
AUTHOR_EMAIL = "shalinvachheta2016@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarizer using GPT-3",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    # python_requires=">=3.6",

)

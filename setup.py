import setuptools

with open("README.md" , "r" , encoding="utf-8" ) as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Text_Summarizer-"
AUTHOR_USER_NAME = "kavish-shrimal"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "kavishshrimali1234@gmail.com"

# THE FINAL CODE FOR THE LOCAL PACKAGE SETUP 
# FIND THE CONSTRUCTER(__INIT__ FILE IN  EVERY FOLDER) AND INSTALL IT IN THEIR LOCATION 
# WE CAN INSTALL IT BY INSTALLING REQ.TXT FILE AND ADDING A COMMAND E . IN REQ.TXT FILE

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
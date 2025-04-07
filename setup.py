from setuptools import setup, find_packages

with open("README.md","r", encoding = "utf-8") as f:
    long_description = f.read()

REPO_NAME = 'ML based skincare recommender system'
AUTHOR_NAME  = 'shivani virang'
RSC_REPO = 'skincare_recommender' 
LIST_OF_REQUIREMENTS = []

setup(
    name = RSC_REPO,
    version = "0.0.1",
    author = "shivani virang",
    description = "A small package for ML based skincare recommendation system ",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/shivani983/skincare-recommendation-system",
    author_email = "shivani_2312res617@iitp.ac.in",
    packages = find_packages(),
    license = "MIT",
    python_requires = ">=3.10",
    install_requires = LIST_OF_REQUIREMENTS

)
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Calculadora",
    version="0.0.1",
    author="Eduardo Matheus",
    author_email="eduardomatheus2306@gmail.com",
    description="Calculadora com Python",
    long_description=page_description,
    long_description_content_type="Python",
    url="my_github_repository_project_link"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
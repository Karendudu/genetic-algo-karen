from setuptools import setup, find_packages

setup(
    name="genetic-algo-karen",
    version="0.1.0",
    author="Karen Dayana",
    author_email="karendayana@example.com",
    description="Librería simple de algoritmos genéticos en Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Karendudu/genetic-algo-karen",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
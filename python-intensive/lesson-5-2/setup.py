from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    description="A useful package for string and data manipulation",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-username/python-intensive",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

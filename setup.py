import setuptools

with open("README.md", "r") as readme:
    long_desc = readme.read()

setuptools.setup(
    name="LGPy",
    version="1.0.2",
    author="NateRiz",
    author_email="nathan.rizik@gmail.com",
    description="A Linear Genetic Programming Library",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/nateriz/lgpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)

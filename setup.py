from setuptools import setup

setup(
    name = "mirrory",
    packages = ["mirrory"],
    install_requires = ["pyyaml", "requests"],
    entry_points = {
        "console_scripts": ['mirrory = mirrory.mirrory:main']
        },
    version = "0.1.0",
    description = "Mirrors a given file to a bunch of free hosts. Work in progress",
    author = "Steven Smith",
    author_email = "stevensmith.ome@gmail.com",
    license = "MIT",
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        ],
    )

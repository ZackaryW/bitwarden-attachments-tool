from setuptools import setup

setup(
    name="bw-util",
    version="1.0",
    author="Zackary W",
    license="MIT",
    url="https://github.com/ZackaryW/bitwarden-attachments-tool",
    long_description=''.join(open('README.md').readlines()),
    long_description_content_type="text/markdown",
    description="A simple utility that wraps bitwarden-cli",
    data_files=["bwexport.py"],
    keywords=["bitwarden", "utility"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "click",
    ],  
    entry_points={
        "console_scripts": [
            'bw-export = bwexport:cli',
        ],
    }

)
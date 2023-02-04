from setuptools import find_packages,setup

from typing import List

def get_requirenments()->List[str]:
    with open(REQUIRENMENT_FILE_NAME) as requirenment_file:

    


setup(
    name="sensors",
    version = "0.0.1",
    author = "ineuron",
    author_email = "kchaple9@gmial.com",
    packages = find_packages(),
    install_requires = get_requirenments(),
)

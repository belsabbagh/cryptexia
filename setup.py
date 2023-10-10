from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "A simple package to encrypt and decrypt basic ciphers."

setup(
    name="cryptexia",
    version=VERSION,
    author="Belal Elsabbagh",
    author_email="<belsabbagh@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=["numpy"],
    keywords=["cryptography", "ciphers", "encryption", "decryption"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

import setuptools

'''
with open("README.md", "r") as fh:
    long_description = fh.read()
'''
long_description = ""

setuptools.setup(
    name='randominfo',
    version='0.1',
    scripts=['randominfo'] ,
    author="Bhuvan Gandhi",
    author_email="bhuvan12501@gmail.com",
    description="Random data generator for IDs, names, emails, passwords, dates, numbers, addresses, images, OTPs etc. for dummy entries.",
    url="https://github.com/bmg02/randominfo",
    download_url = 'https://github.com/bmg02/randominfo/dist/randominfo-0.1.tar.gz',
    packages=setuptools.find_packages(),
    install_requires = ["PIL", "csv", "pytz", "glob"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
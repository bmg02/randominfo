import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='randominfo',
    version='2.0.2',
    packages=['randominfo'],
    author="Bhuvan Gandhi",
    author_email="bhuvan12501@gmail.com",
    description="Random data generator for IDs, names, emails, passwords, dates, numbers, addresses, images, OTPs etc. for dummy entries.",
    long_description = long_description,
    long_description_content_type='text/markdown',
    package_data={
        'randominfo': ['data.csv', 'images/people/*.jpg']
    },
    url="https://github.com/bmg02/randominfo",
    download_url = 'https://github.com/bmg02/randominfo/dist/randominfo-2.0.2.tar.gz',
    python_requires='>=3',
    install_requires = ["pillow>=5.4.1", "pytz>=2018.5"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
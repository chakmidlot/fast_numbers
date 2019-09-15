import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fast_numbers-chakmidlot",
    version="0.0.1",
    author="Dzmitry Talkach",
    author_email="chakmidlot@gmail.com",
    description="Training game to remember numbers fast",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chakmidlot/fast_numbers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': ['fast_numbers=fast_numbers.game:main']
    }
)

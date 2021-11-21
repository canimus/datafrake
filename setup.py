import setuptools

setuptools.setup(
    name="datafrake",
    version="0.0.1",
    description="A dataframe data generator inspired by APL programming language",
    author="Herminio Vazquez",
    author_email="canimus@gmail.com",
    url="https:/github.com/canimus/datafrake.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Data Engineers",
        "Operative System :: Linux",
        "Topic :: Data",
        "Topic :: Schemas",
        "Topic :: Validation",
    ],
    include_package_data=True,
    python_requires=">=3.8"
)

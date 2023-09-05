from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ninetydf",
    version="0.1",
    description="90 Day Fiancé dataframes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/90df/ninetydf",
    author="ninety",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "pandas",
        'importlib_resources; python_version<"3.9"',
    ],
    tests_require=["pytest"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
    ],
)

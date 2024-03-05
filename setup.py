import pathlib

import setuptools

setuptools.setup(
    name="pysorters",
    version="0.5.3",
    author="yo1",
    author_email="bigdiebam@gmail.com",
    description="A package with all sorting algorithms.",
    long_description=pathlib.Path("C:\\pysorters_project\\README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/yo1am1/pysorters",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10, <=3.12",
    project_urls={
        "Source": "https://github.com/yo1am1/pysorters",
    },
    install_requires=[
        "pytest",
    ],
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "sorting algorithms",
        "bubble sort",
        "merge sort",
        "quick sort",
        "insertion sort",
        "selection sort",
        "heap sort",
        "radix sort",
        "counting sort",
        "bucket sort",
        "sort",
        "sorting",
        "algorithms",
        "python",
        "pysorters_project",
    ],
)

from distutils.util import convert_path
from setuptools import find_packages, setup

module_name = "iocontroller"
main_ns = {}
ver_path = convert_path(f"src/{module_name}/version.py")
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name=module_name,
    version=main_ns["__version__"],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    license="MIT",
    description="Python IO controller tools",
    keywords=["keyboard", "mouse"],
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf8").read(),
    install_requires=[
        "swig==4.1.1",
        "pywin32==305",
        "pyWinhook==1.6.2",
        "pyperclip==1.8.2",
        "pygetwindow==0.0.9",
    ],
    url="https://github.com/tassoneroberto/iocontroller",
    author="Roberto Tassone",
    author_email="roberto.tassone@proton.me",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)

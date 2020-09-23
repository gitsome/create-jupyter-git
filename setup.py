import sys
import pathlib
from setuptools import setup

python_requires='>=3.5'

if sys.version_info < (3, 5):
    raise RuntimeError("This package requres Python 3.5+")

HERE = pathlib.Path(__file__).parent
long_description = (HERE / "README.md").read_text()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='create-jupyter-git',
    version='0.0.2',
    description='A CLI command that generates a fresh Git Repository with files and configs to optimize version control for Jupyter Notebooks',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gitsome/create-jupyter-git",
    author='John Martin',
    author_email='johndavidfive@gmail.com',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    packages=['create_jupyter_git'],  
    include_package_data=True,
    install_requires=requirements, 
    entry_points={
        'console_scripts': ['create-jupyter-git=create_jupyter_git.setup_notebook_version_control:generate_repo']
    }
)
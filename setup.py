import sys
from setuptools import Extension, setup

python_requires='>=3.5'

if sys.version_info < (3, 5):
    raise RuntimeError("This package requres Python 3.5+")

setup(
    name='create-jupyter-git',
    version='1.0',
    description='A CLI command that generates a fresh Git Repository with files and configs to optimize version control for Jupyter Notebooks',
    long_description=open('README.md', 'r').read(),
    author='John Martin',
    author_email='johndavidfive@gmail.com',
    packages=['jupyter_git_filter'],  
    install_requires=[], 
    entry_points={
        'console_scripts': ['create-jupyter-git=jupyter_git_filter.setup_notebook_version_control:main']
    }
)
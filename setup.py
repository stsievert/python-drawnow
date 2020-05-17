from setuptools import setup
from os import path

# Steps to update on PyPI:
# 1. python setup.py sdist bdist_wheel
# 2. twine upload dist/*

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), "r") as f:
    long_description = f.read()

setup(
    name='drawnow',
    packages=['drawnow'],
    version='0.72.5',
    description='MATLAB-like drawnow',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Scott Sievert',
    author_email='dev@stsievert.com',
    url='https://github.com/stsievert/python-drawnow',
    download_url='https://github.com/stsievert/python-drawnow/archive/master.zip',
    keywords=['figure', 'plotting', 'visualization', 'matlab'],
    use_2to3=True,
    requires=['matplotlib'],
    install_requires=['matplotlib>=1.5'],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English", "Operating System :: OS Independent",
        "Programming Language :: Python", "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization"
    ])

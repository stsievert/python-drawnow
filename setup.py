from setuptools import setup

# Steps to update on PyPI:
# 1. python setup.py sdist bdist_wheel
# 2. twine upload dist/*

setup(
    name='drawnow',
    packages=['drawnow'],
    version='0.71.4',
    description='MATLAB-like drawnow',
    author='Scott Sievert',
    author_email='stsievert@wisc.edu',
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

from setuptools import setup
setup(name         = 'drawnow',
      packages     = ['drawnow'],
      version      = '0.71.2',
      description  = 'MATLAB-like drawnow',
      author       = 'Scott Sievert',
      author_email = 'stsievert@wisc.edu',
      url          = 'https://github.com/scottsievert/python-drawnow',
      download_url = 'https://github.com/scottsievert/python-drawnow/archive/master.zip',
      keywords     = ['figure', 'plotting', 'visualization', 'matlab'],
      use_2to3     = True,
      requires     = ['matplotlib'],
      classifiers  = [
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Scientific/Engineering",
          "Topic :: Scientific/Engineering :: Visualization"
      ])

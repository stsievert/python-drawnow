from setuptools import setup
setup(
  name             = 'drawnow',
  packages         = ['drawnow'],
  version          = '0.54',
  description      = 'MATLAB-like drawnow',
  author           = 'Scott Sievert',
  author_email     = 'sieve121@umn.edu',
  url              = 'https://github.com/scottsievert/python-drawnow',
  download_url     = 'https://github.com/scottsievert/python-drawnow/archive/master.zip',
  keywords         = ['figure', 'plotting', 'visualization', 'matlab'],
  requires = ['matplotlib'],
  classifiers  = [
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Scientific/Engineering",
          "Topic :: Scientific/Engineering :: Visualization"
      ],
)

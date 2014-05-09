from distutils.core import setup
setup(
  name         = 'drawnow',
  packages     = ['drawnow'], # this must be the same as the name above
  version      = '0.41',
  description  = 'MATLAB-like drawnow',
  author       = 'Scott Sievert',
  author_email = 'sieve121@umn.edu',
  url          = 'https://github.com/scottsievert/python-drawnow',
  download_url = 'https://github.com/scottsievert/python-drawnow/archive/master.zip',
  keywords     = ['figure', 'plotting', 'visualization', 'matlab'],
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

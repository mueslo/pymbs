from setuptools import setup

setup(name='mbs',
      version='0.2',
      description='Utilities for MB Scientific analyzer data',
      url='http://github.com/mueslo/mbs',
      author='mueslo',
      author_email='mueslo@mueslo.de',
      license='GPLv3',
      packages=['mbs'],
      install_requires=[
          'numpy',
          'scipy',
          'matplotlib~=3.4',
          'pandas',
      ],
      extras_require={
          'xarray': ["xarray"],
          'widgets': ["jupyterlab~=3.2", "ipympl~=0.8", "ipywidgets~=7.6"]
      },
      zip_safe=False)
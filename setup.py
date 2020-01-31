from setuptools import setup, Command
import os
import sys

setup(name='atspy',
      version='1.3',
      description='Automated Time Series in Python',
      url='https://github.com/firmai/automated-time-series',
      author='snowde',
      author_email='d.snow@firmai.org',
      license='MIT',
      packages=['atspy','atspy.TS'],
      install_requires=[
          'pandas',
          'numpy==1.17.4',
          'scipy',
          'numba',
          'datetime',
          'pmdarima',
          'pydot',
          'dill',
          'pathos',
          'sqlalchemy',
          'matplotlib',
          'xgboost',
          'sklearn',
          'mxnet==1.4.1',
          'gluonts',
          'nbeats-pytorch',
          'python-dateutil==2.8.0'

      ],
      zip_safe=False)

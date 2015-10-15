from setuptools import setup

setup(name='Slow Tests',
      entry_points={
          'nose.plugins.0.10': [
              'slowtests= slow_tests:SlowTests'
          ]
      },
      )


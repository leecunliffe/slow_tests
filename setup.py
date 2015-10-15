from setuptools import setup

setup(name='SlowTests',
      entry_points={
          'nose.plugins.0.10': [
              'slowtests= slow_tests:SlowTests'
          ]
      },
      author="Yellowbeard",
      author_email="artbasher@gmail.com",
      url="https://github.com/yellow-beard/slow_tests",
      description="Plugin for noset that identifies and prints your slowest tests"
      )


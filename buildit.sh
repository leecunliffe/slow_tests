#!/bin/bash
python setup.py sdist
twine upload dist/*
rm -rf SlowTests.egg-info/ dist/

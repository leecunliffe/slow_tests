# Slow Tests


Plugin for python's nose http://nose.readthedocs.org/ that prints your slowest tests.

To install:

`pip install -e git+https://github.com/yellow-beard/slow_tests.git#egg=slow_tests`

Then you can run your tests like this:

`nosetests --with-slowtests path_to_your_tests/your_test.py`

And at the end of the test run, you'll see some pretty output with test times and names so you can identify your slow tests and speed them up :)




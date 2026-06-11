# pre-request: install  a pytest plugin "pytest-xdist" to run the parallel testing

# to install : pip install pytest-xdist
#  "-n" is represents no.of workers

def test_one():
    print("Running test one")
    assert True

def test_two():
    print("Running test two")
    assert True

def test_three():
    print("Running test three")
    assert True

def test_four():
    print("Running test four")
    assert True
#  pytest Day-17/test_parallel.py -s -v -n 2 or -n=2    "-n" is represents no.of workers can split the test cases and execute at a time.



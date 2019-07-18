import os
import unittest


if __name__ == '__main__':
	os.environ['UNITTESTING'] = '1'

	tests = unittest.TestLoader().discover('./Tests')
	unittest.TextTestRunner(verbosity=2).run(tests)

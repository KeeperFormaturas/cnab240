from Tests.ItauFileTestCase import ItauFileTestCase
import os
import unittest


if __name__ == '__main__':
	os.environ['UNITTESTING'] = '1'
	suite = unittest.TestLoader().loadTestsFromTestCase(ItauFileTestCase)
	unittest.TextTestRunner(verbosity=2).run(suite)

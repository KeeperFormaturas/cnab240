from Tests.ItauFileTestCase import ItauFileTestCase
import unittest

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(ItauFileTestCase)
	unittest.TextTestRunner(verbosity=2).run(suite)

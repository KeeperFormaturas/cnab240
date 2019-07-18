from keeper_cnab240.file import File
import os
import unittest


class TestItauReturn(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def test_process_return_file():
        file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'TEST.RET'), 'r')
        file_content = file.read()
        file.close()

        payment_file = File('Itau')
        payment_file.read_file_content(file_content)

        assert len(payment_file.payments) == 1
        assert payment_file.payments[0].status().is_error is False
        assert payment_file.payments[0].status().is_processed is True
        assert payment_file.payments[0].get_attribute('amount') == '0000102941'


if __name__ == '__main__':
    unittest.main()

from keeper_cnab240.banks.Itau.payment_methods import PaymentMethods
from Tests.Utils.Companies import company
from Tests.Utils.Payments import payments
from Tests.Utils.Utils import hash_file, payment_file_generator
import os
import unittest


class TestItauPaymentA(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def test_process_one_paymentA():
        _payments = payments(PaymentMethods.TED)
        body_big_line = payment_file_generator('Itau', company, [_payments['A1']])
        root_path = os.path.dirname(os.path.abspath(__file__))
        body_big_file_path = os.path.join(root_path, 'body_big_file_segment_a.rem')

        f = open(body_big_file_path, 'w')
        f.write(body_big_line)
        f.close()

        file_hash = hash_file(body_big_file_path, True)
        os.remove(body_big_file_path)

        assert 'c18667af379b1522b163170b7e8825540fe3f162365cef78cce91bbf5c92c56b' == file_hash


if __name__ == '__main__':
    unittest.main()

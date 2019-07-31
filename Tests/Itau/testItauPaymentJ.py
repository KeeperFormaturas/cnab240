from keeper_cnab240.banks.Itau.payment_methods import PaymentMethods
from Tests.Utils.Companies import company
from Tests.Utils.Payments import payments
from Tests.Utils.Utils import hash_file, payment_file_generator
import os
import unittest


class TestItauPaymentJ(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def test_process_one_paymentJ():
        _payments = payments(payment_method_j=PaymentMethods.BOLETOS_OUTROS_BANCOS)
        body_big_line = payment_file_generator('Itau', company, [_payments['J']])
        root_path = os.path.dirname(os.path.abspath(__file__))
        body_big_file_path = os.path.join(root_path, 'body_big_file_segment_j.rem')

        f = open(body_big_file_path, 'w')
        f.write(body_big_line)
        f.close()

        file_hash = hash_file(body_big_file_path, True)
        os.remove(body_big_file_path)

        assert '1b4564e2f0fd9847e13850ecae46cdde60a76c7581c2c2c8bef5f2afb60eb090' == file_hash


if __name__ == '__main__':
    unittest.main()

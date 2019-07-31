from keeper_cnab240.banks.Itau.payment_methods import PaymentMethods
from Tests.Utils.Companies import company
from Tests.Utils.Payments import payments
from Tests.Utils.Utils import hash_file, payment_file_generator
import os
import unittest


class TestItauMultiPayment(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def test_process_multi_payments():
        _payments = payments(PaymentMethods.TED, PaymentMethods.BOLETOS_OUTROS_BANCOS)
        body_big_line = payment_file_generator('Itau', company, [_payments['A1'], _payments['J']])

        root_path = os.path.dirname(os.path.abspath(__file__))
        body_big_file_path = os.path.join(root_path, 'multpay.rem')

        f = open(body_big_file_path, 'w')
        f.write(body_big_line)
        f.close()

        file_hash = hash_file(body_big_file_path, True)
        os.remove(body_big_file_path)

        assert '1a2bf7358e6aadf2814d8d8b80a4ab58f4dbeb3e9923ad7e53b2644d6786415a' == file_hash


if __name__ == '__main__':
    unittest.main()

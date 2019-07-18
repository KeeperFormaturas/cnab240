from .ItauUtils import company, company_j
from pg_cnab240.banks.Itau.payment_methods import PaymentMethods
from pg_cnab240.file import File
from pg_cnab240.payment import Payment
import os
import unittest
import Tests.Utils as Utils


class TestItauPaymentJ(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def test_process_one_paymentJ():
        payment_file = File('Itau', company)
        payment_file.header.set_company_data(company)
        payment_file.payments = []

        payment = Payment(type=PaymentMethods.BOLETOS_OUTROS_BANCOS,
                          favored_name=company_j.name,
                          favored_bank=company_j.bank_account.bank_code,
                          agency=company.bank_account.agency,
                          account=company.bank_account.account,
                          account_digit=company.bank_account.digit,
                          pay_date='05072019',
                          currency_type=9,
                          dv='3',
                          due_rule='7941',
                          amount=1029.41,
                          free_field='0296090001270557500010810',
                          due_date='05072019',
                          title_amount=1029.41,
                          payment_amount=1029.41,
                          your_number='12345678901234567890',
                          recipient_document_type=2,
                          recipient_document_number=20093235000182,
                          recipient_name=company_j.name)

        payment_file.add_payment(payment)
        payment_file.generate()
        body_big_line = payment_file.get_content()

        root_path = os.path.dirname(os.path.abspath(__file__))
        body_big_file_path = os.path.join(root_path, 'body_big_file_segment_j.rem')

        f = open(body_big_file_path, 'w')
        f.write(body_big_line)
        f.close()

        file_hash = Utils.hash_file(body_big_file_path, True)
        os.remove(body_big_file_path)

        assert '1b4564e2f0fd9847e13850ecae46cdde60a76c7581c2c2c8bef5f2afb60eb090' == file_hash


if __name__ == '__main__':
    unittest.main()

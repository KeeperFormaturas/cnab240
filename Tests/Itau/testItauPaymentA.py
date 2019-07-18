from .ItauUtils import company, company_j
from keeper_cnab240.banks.Itau.payment_methods import PaymentMethods
from keeper_cnab240.file import File
from keeper_cnab240.payment import Payment
import os
import Tests.Utils as Utils
import unittest


class TestItauPaymentA(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def test_process_one_paymentA():
        payment_file = File('Itau', company)
        payment_file.header.set_company_data(company)
        payment_file.payments = []

        payment = Payment(type=PaymentMethods.TED,
                          favored_name=company_j.name,
                          favored_bank=company_j.bank_account.bank_code,
                          agency=company.bank_account.agency,
                          account=company.bank_account.account,
                          account_digit=company.bank_account.digit,
                          your_number='n1U0fXg4Tl2RLotU0YQ8',
                          pay_date='01012019',
                          payment_amount=2400.00,
                          favored_document_number=company_j.document)
        payment_file.add_payment(payment)
        payment_file.generate()
        body_big_line = payment_file.get_content()

        root_path = os.path.dirname(os.path.abspath(__file__))
        body_big_file_path = os.path.join(root_path, 'body_big_file_segment_a.rem')

        f = open(body_big_file_path, 'w')
        f.write(body_big_line)
        f.close()

        file_hash = Utils.hash_file(body_big_file_path, True)
        os.remove(body_big_file_path)

        assert 'b31957cda8950105f0e659b9ed70ecc01ef1aee253e59d56d3596d6ffc6aed93' == file_hash


if __name__ == '__main__':
    unittest.main()

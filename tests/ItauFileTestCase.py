import unittest
from pg_cnab240.file import File
from pg_cnab240.company import Company
from pg_cnab240.payment import Payment
from datetime import datetime
import os

# create company object
company = Company('BF Servicos De Cobranca Ltda', '07179434000140')
company.set_bank_acccount(341, '00772', '69637', 3)
company.set_address('Av. Andrômeda', 2000, 'Bl.8-4 andar', 'Alphaville Residencial Plus', 'Barueri', 'SP', '06473000')

class ItauFileTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_1_generate_header(self):
        payment_file = File('itau', company)
        payment_file.header.set_company_data(company)
        header_line = payment_file.header.to_line()
        # print(header_line)
        # print(len(header_line))
        assert '240' in str(len(header_line))
    
    def test_2_process_one_paymentA(self):
        payment_file = File('itau', company)
        payment_file.header.set_company_data(company)

        payment = Payment(payment_type='ted', favored_name='felipe lucifero rosado eventos', favored_bank='033', agency='03875', account='000013006629', account_digit=0, your_number='5511972063805440', pay_date='10052018', ispb_code='90400888', payment_amount=2400.00, favored_document_number='21044237000144')

        # add payment
        payment_file.add_payment(payment)

        # generate
        payment_file.generate()

        body_big_line = ''.join(payment_file.body)

        root_path = os.path.dirname(os.path.abspath(__file__))
        body_big_file_path = os.path.join(root_path, 'body_big_file.txt')
        f = open(body_big_file_path, 'w')
        f.write(body_big_line)
        f.close()

        assert '34100011C2041040 207179434000140                    03875 000013006629 3BF SERVICOS DE COBRANCA LTDA                                          AV ANDROMEDA                  02000BL84 ANDAR     BARUERI             06473000SP                  3410001300001A00000003303875 000013006629 0FELIPE LUCIFERO ROSADO EVENTOS5511972063805440    10052018REA904008880000000000000000240000                            000000000000000                    00000021044237000144                       34100015         000003000000000000240000000000000000000000                                                                                                                                                                                     ' in body_big_line


if __name__ == '__main__':
    unittest.main()
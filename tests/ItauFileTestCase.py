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

    payment_file = None
    payment = None

    def setUp(self):
        self.payment_file = File('itau', company)
        self.payment_file.header.set_company_data(company)

    def tearDown(self):
        self.payment_file = None
        self.payment = None
    
    def test_1_generate_header(self):
        self.payment_file.header.set_company_data(company)
        header_line = self.payment_file.header.to_line()
        # print(header_line)
        # print(len(header_line))
        assert '240' in str(len(header_line))
    
    def test_2_process_one_paymentA(self):
        self.payment = Payment(type='ted', favored_name='Cliente Teste', favored_bank='033', agency='01111', account='000011111111', account_digit=0, your_number='5511972063805440', pay_date='10052018', ispb_code='90400888', payment_amount=2400.00, favored_document_number='11111111111111')

        # add payment
        self.payment_file.add_payment(self.payment)

        # generate
        self.payment_file.generate()

        body_big_line = ''.join(self.payment_file.body)

        root_path = os.path.dirname(os.path.abspath(__file__))
        body_big_file_path = os.path.join(root_path, 'body_big_file_segment_a.txt')
        f = open(body_big_file_path, 'w')
        f.write(body_big_line)
        f.close()

        assert '34100011C2041040 207179434000140                    01111 000011111111 3BF SERVICOS DE COBRANCA LTDA                                          AV ANDROMEDA                  02000BL84 ANDAR     BARUERI             06473000SP                  3410001300001A00000003301111 000011111111 0CLIENTE TESTE                 5511972063805440    10052018REA904008880000000000000000240000                            000000000000000                    00000011111111111111                       34100015         000003000000000000240000000000000000000000                                                                                                                                                                                     ' in body_big_line
    
    def test_3_process_one_paymentJ(self):
        self.payment = Payment(type='slip', favored_name='Cliente Teste', favored_bank='033', pay_date='10052018', ispb_code='90400888', currency_type=9, dv='4', due_rule='7524', amount=10067.60, free_field='9485239700000007661190101', due_date='14052018', title_amount=10067.60, payment_amount=10067.60, your_number='5506715023835136')

        # add payment
        self.payment_file.add_payment(self.payment)

        # generate
        self.payment_file.generate()

        body_big_line = None
        body_big_line = ''.join(self.payment_file.body)

        root_path = os.path.dirname(os.path.abspath(__file__))
        body_big_file_path = os.path.join(root_path, 'body_big_file_segment_j.txt')
        f = open(body_big_file_path, 'w')
        f.write(body_big_line)
        f.close()

        assert '34100011C2031080 207179434000140                    00772 000000020070 5BF SERVICOS DE COBRANCA LTDA                                          Av Andromeda                  02000Bl84 andar     Barueri             06473000SP                  3410001300001J00003394752400010067609485239700000007661190101CLIENTE TESTE                 14052018000000001006760000000000000000000000000000000100520180000000010067600000000000000005506715023835136                                          34100015         000003000000000001006760000000000000000000                                                                                                                                                                                     ' in body_big_line


if __name__ == '__main__':
    unittest.main()
import unittest
from pg_cnab240.file import File
from pg_cnab240.company import Company
from pg_cnab240.payment import Payment
from datetime import datetime

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
        payment_file.header.set_data(company)
        header_line = payment_file.header.to_line()
        # print(header_line)
        # print(len(header_line))
        assert '240' in str(len(header_line))
    
    def test_2_process_one_paymentA(self):
        payment_file = File('itau', company)
        payment_file.header.set_data(company)

        payment = Payment(payment_type='ted', favored_name='felipe lucifero rosado eventos', favored_bank='033', agency='03875', account='000013006629', account_digit=0, your_number='5511972063805440', pay_date='10052018', ispb_code='90400888', payment_amount=2400.00, favored_document_number='21044237000144')

        # add payment
        payment_file.add_payment(payment)

        # process payment
        payment_file.process_payments()

        assert '34100031C2041080 207179434000140                    00772 000000020070 5BF SERVICOS DE COBRANCA LTDA                                          Av Andromeda                  02000Bl84 andar     Barueri             06473000SP                  3410003300001A00000003303875 000013006629 0felipe lucifero rosado eventos5511972063805440    10052018REA904008880000000000000000240000                    00000000000000000000000                    00000021044237000144                       34100035         000003000000000000240000000000000000000000                                                                                                                                                                                     ' in ''


if __name__ == '__main__':
    unittest.main()
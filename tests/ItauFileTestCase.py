import unittest
from pg_cnab240.file import File
from pg_cnab240.company import Company
from pg_cnab240.payment import Payment

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
        print(header_line)
        print(len(header_line))
        assert '240' in str(len(header_line))


if __name__ == '__main__':
    unittest.main()
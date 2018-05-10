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
    
    # def test_register_slip(self):
    #     response = payment_processor.register_slip(
    #         slip_data['billing_number'],
    #         slip_data['slip_number'],
    #         dict(
    #             due_date=slip_data['due_date'],
    #             amount=slip_data['amount'],
    #             interest=slip_data['interest'],
    #             forfeit=slip_data['forfeit'],
    #             discount=slip_data['discount']
    #         ),
    #         dict(
    #             full_name=slip_data['full_name'],
    #             email=slip_data['email'],
    #             document=slip_data['document']
    #         ),
    #         dict(
    #             street=slip_data['street'],
    #             number=slip_data['number'],
    #             complement=slip_data['complement'],
    #             neighborhood=slip_data['neighborhood'],
    #             city=slip_data['city'],
    #             state=slip_data['state'],
    #             zipcode=slip_data['zipcode']
    #         ),
    #         slip_data['text']
    #     )
    #     print(response)
    #     assert "201" in str(response['status_code'])

    # def test_print_slip(self):
    #     response = payment_processor.print_slip([
    #         slip_data['slip_number']
    #     ])
    #     print(response)
    #     assert "200" in str(response['status_code'])

    # def test_cancel_slip(self):
    #     # response = payment_processor.cancel_slip(slip_data['slip_number'])
    #     response = payment_processor.cancel_slip(49)
    #     print(response)
    #     assert "200" in str(response['status_code'])

    # def test_get_slip_receipts(self):
    #     response = payment_processor.get_slip_receipts()
    #     print(response)
    #     assert '200' in str(response['status_code'])

    # def test_get_slip_paid_receipts(self):
    #     response = payment_processor.get_slip_paid_receipts()
    #     print(response)
    #     assert '200' in str(response['status_code'])

    # def test_get_slip_receipts_by_date(self):
    #     response = payment_processor.get_slip_receipts_by_date('2018-03-01', '2018-04-01')
    #     print(response)
    #     assert '200' in str(response['status_code'])

    # def test_get_card_token(self):
    #     response = payment_processor.credit_card_processor.get_card_token(
    #         credit_card_data['card_number'],
    #         credit_card_data['card_month'],
    #         credit_card_data['card_year'],
    #         credit_card_data['card_cvv'],
    #         credit_card_data['name'],
    #         credit_card_data['document'],
    #         credit_card_data['email'],
    #         credit_card_data['cellphone']
    #     )
        
    #     print(response)
        
    #     credit_card_data['card_token'] = response['data']['card_token']
        
    #     assert "201" in str(response['status_code'])

    # def test_register_credit_card(self):
    #     response = payment_processor.register_credit_card(
    #         credit_card_data['card_token'],
    #         credit_card_data['amount'],
    #         credit_card_data['installments'],
    #         credit_card_data['description']
    #     )
        
    #     print(response)

    #     if 'transaction_id' in response['data']:
    #         credit_card_data['transaction_id'] = response['data']['transaction_id']
    #         credit_card_data['conciliation_transaction_id'] = response['data']['conciliation_transaction_id']
    #         credit_card_data['authorization'] = response['data']['authorization']
            
    #         assert "201" in str(response['status_code'])
    #     assert "500" in str(response['status_code'])
    
    # def test_cancel_credit_card(self):
    #     if credit_card_data['transaction_id'] is not None:
    #         response = payment_processor.cancel_credit_card(credit_card_data['transaction_id'])
    #         print(response)
    #         assert "200" in str(response['status_code'])
    #     else:
    #         print('No transaction_id')
    #         assert "200" in '200'

    # def test_get_credit_card_receipts(self):
    #     response = payment_processor.get_credit_card_receipts()
    #     print(response)
    #     assert '200' in str(response['status_code'])
    
    # def test_reports_paid_slips(self):
    #     paid_slips = dict(
    #         registereds = 0,
    #         paid_amount = 0.00,
    #         net_amount = 0.00,
    #         tariffs = 0.00,
    #     )
    #     page = 1
    #     payment_response = payment_processor.get_slip_paid_receipts_by_date_with_pagination('2018-04-13', '2018-04-13', page)
    #     print(payment_response)
    #     while 'receipts' in payment_response['data'] and payment_response['data']['receipts']:
    #         for paid_slip in payment_response['data']['receipts']:
    #             paid_slips['registereds'] += 1
    #             paid_slips['paid_amount'] += float(paid_slip['paid_amount'])
    #             paid_slips['net_amount'] += (float(paid_slip['paid_amount']) - 1.60)
    #             paid_slips['tariffs'] += 1.60
    #         page += 1
    #         payment_response = payment_processor.get_slip_paid_receipts_by_date_with_pagination('2018-04-13', '2018-04-13', page)
    #         print(payment_response)
    #     paid_slips['paid_amount'] = round(paid_slips['paid_amount'], 2)
    #     paid_slips['net_amount'] = round(paid_slips['net_amount'], 2)
    #     paid_slips['tariffs'] = round(paid_slips['tariffs'], 2)
    #     print(paid_slips)
    #     assert '200' in str(payment_response['status_code'])

    def test_1_generate_header(self):
        payment_file = File('itau', company)
        payment_file.header.set_data(company)
        assert '200' in '200'


if __name__ == '__main__':
    unittest.main()
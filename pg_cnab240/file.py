from pydoc import locate

class File:
    def __init__(self, bank, company=None, payments=[]):
        self.company = company
        self.payments = payments

        self.bank = self.import_bank(bank)
        self.header = self.import_header()
        self.footer = self.import_footer()
        self.count_lots = 1
    
    def import_bank(self, bank):
        bankClassFile =  locate('pg_cnab240.banks.' + bank + '.' + bank)
        bankClass = getattr(bankClassFile, bank)
        return bankClass()

    def import_header(self):
        return self.bank.get_file_header()
    
    def import_footer(self):
        return self.bank.get_file_footer()
    
    def verify(self):
        if self.header is None or self.footer is None:
            raise Exception('Header and Footer cannot be None')
        return True
    
    def add_payment(self, payment):
        self.payments.append(payment)
    
    def process_payments(self):
        for payment in self.payments:
            # get bank payment segment
            payment_segment = self.bank.get_payment_segment(payment.get_attribute('payment_type'))
            segment = payment_segment['segment_class']()
            segment.set_bank(self.bank)
            segment.set_company(self.company)
            segment_data = payment.attributes
            segment_data['register_number'] = self.count_lots
            segment.set_data(segment_data)

            # increment count_lots
            self.count_lots += 1

    def generate(self):
        self.verify()

        # populate header
        self.header.set_data(self.company)

        # process payments
        self.process_payments()
        pass
    
    def read(self, file_content):
        self.verify()
        pass

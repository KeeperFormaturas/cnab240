import pg_cnab240.banks

class File:
    def __init__(self, bank, payment_type, company=None, payments=[]):
        self.company = company
        self.payments = payments

        self.bank = self.import_bank(bank)
        self.header = self.import_header()
        self.footer = self.import_footer()

        self.segment = self.import_segment(payment_type)
    
    def import_bank(self, bank):
        bankClass =  __import__('banks.' + bank + '.' + bank + '.' + bank)
        return bankClass()

    def import_header(self):
        pass
    
    def import_footer(self):
        pass
    
    def import_segment(self, payment_type):
        pass
    
    def verify(self):
        if self.header is None or self.segment is None or self.footer is None:
            raise Exception('Header, Segment and Footer cannot be None')
        return True

    def generate(self):
        self.verify()

        # populate header
        self.header.set_data(self.company)
        pass
    
    def read(self, file_content):
        self.verify()
        pass

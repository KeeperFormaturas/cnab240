from pydoc import locate

class File:
    def __init__(self, bank, company=None, payments=[]):
        self.company = company
        self.payments = payments

        self.bank = self.import_bank(bank)
        self.header = self.import_header()
        self.footer = self.import_footer()
    
    def import_bank(self, bank):
        bankClass =  locate('pg_cnab240.banks.' + bank + '.' + bank + '.' + bank)
        return bankClass()

    def import_header(self):
        self.header = self.bank.get_file_header()
    
    def import_footer(self):
        self.footer = self.bank.get_file_footer()
    
    def verify(self):
        if self.header is None or self.footer is None:
            raise Exception('Header and Footer cannot be None')
        return True
    
    def process_payments(self):
        # TODO:
        pass

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

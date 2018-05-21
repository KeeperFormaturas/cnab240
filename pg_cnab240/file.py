from pydoc import locate

class File:
    def __init__(self, bank, company=None, payments=[]):
        self.company = company
        self.payments = payments

        self.bank = self.import_bank(bank)
        self.header = self.import_header()
        self.footer = self.import_footer()
        self.body = []
        self.lots_quantity = 1
        self.lines = []
        self.line_cursor = 0
    
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
            register_number = 1
            
            # get bank payment segment
            payment_segment = self.bank.get_payment_segment(payment.get_attribute('type'))
            segment = payment_segment['segment_class']()

            # set bank and company
            segment.set_bank(self.bank)
            segment.set_company(self.company)

            # attr payment attributes
            segment_data = payment.attributes
            segment_data['payment_way'] = payment_segment['payment_types'][payment.get_attribute('type')]
            
            # set custom segment attributes
            segment_data['lot_code'] = self.lots_quantity
            segment_data['register_number'] = register_number
            segment.set_data(segment_data)

            # check header
            if hasattr(segment, 'get_header_line'):
                self.body.append(segment.get_header_line())
            
            self.body.append(segment.to_line())

            # check footer
            if hasattr(segment, 'get_footer_line'):
                self.body.append(segment.get_footer_line())

            # increment lots_quantity
            self.lots_quantity += 1

    def generate(self, file_path=None):
        self.verify()

        # add header line
        self.lines.append(self.header.to_line())

        # process payments
        self.process_payments()

        for line in self.body:
            self.lines.append(line)

        # populate footer
        self.footer.set_data(dict(
            lots_quantity = self.lots_quantity - 1,
            registers_quantity = ((self.lots_quantity - 1) * 3) + 2,
        ))

        # add footer line
        self.lines.append(self.footer.to_line())

        if file_path:
            # generate file
            #TODO:
            pass

        pass
    
    def get_content(self):
        content = ""
        for line in self.lines:
            content += line + "\n"
        return content
    
    def next_line(self):
        if self.line_cursor > (len(self.lines) - 1):
            return None
        line = self.lines[self.line_cursor]
        self.line_cursor += 1
        return line
    
    def read(self, file_content):
        self.verify()
        pass

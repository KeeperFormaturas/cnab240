from pg_cnab240.banks.bank_account import BankAccount


class Company:
    def __init__(self, name, document):
        self.document_type = self.get_company_document_type(document)
        self.document = document

        self.bank_account = None

        # address
        self.street = None
        self.number = None
        self.complement = None
        self.district = None
        self.city = None
        self.state = None
        self.country = None
    
    def set_bank_acccount(self, bank_code, agency, account, account_digit):
        self.bank_account = BankAccount(bank_code, agency, account, account_digit)
    
    def set_address(self, street, number, complement, district, city, state, country='BR'):
        self.street = street
        self.number = number
        self.complement = complement
        self.district = district
        self.city = city
        self.state = state
        self.country = country
    
    def get_company_document_type(self, document_number):
        if len(str(document_number)) == 14:
            return 'cnpj'
        return 'cpf'

from pg_cnab240.banks.bank import Bank
from pg_cnab240.banks.itau.file_header import FileHeader
from pg_cnab240.banks.itau.file_footer import FileFooter
from pg_cnab240.banks.itau.segments.A import SegmentA, SegmentANF
from pg_cnab240.banks.itau.segments.J import SegmentJ


class itau(Bank):
    def __init__(self):
        super().__init__('Itaú', 'itau', 341)
    
    def get_file_header(self):
        file_header = FileHeader()
        file_header.set_bank(self)
        return file_header
    
    def get_file_footer(self):
        return FileFooter()
    
    def get_company_document_id(self, document_type):
        if document_type == 'cnpj':
            return 2
        return 1 # cpf
    
    def get_payment_segment(self, payment_type):
        if payment_type == 'slip':
            return 'J'
        elif payment_type == 'doc' or payment_type == 'ted' or payment_type == 'transfer' or payment_type == 'tedd':
            return 'A'
        elif payment_type == 'nf':
            return 'ANF'
        return None
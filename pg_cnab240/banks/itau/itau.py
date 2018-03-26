from pg_cnab240.banks.bank import Bank
from pg_cnab240.banks.itau.file_header import FileHeader
from pg_cnab240.banks.itau.file_footer import FileFooter
from pg_cnab240.banks.itau.segments.A import SegmentA, SegmentANF
from pg_cnab240.banks.itau.segments.J import SegmentJ


class itau(Bank):
    def __init__(self):
        super().__init__('Itaú', 'itau', 341)
    
    def get_file_header(self):
        return FileHeader()
    
    def get_company_document_type(self, document_number):
        document_type = super().get_company_document_type(document_number)
        if document_type == 'cnpj':
            return 2
        return 1 # cpf
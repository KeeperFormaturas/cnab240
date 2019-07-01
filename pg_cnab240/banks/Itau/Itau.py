from pg_cnab240.banks.bank import Bank
from pg_cnab240.banks.Itau.file_header import FileHeader
from pg_cnab240.banks.Itau.file_footer import FileFooter
from pg_cnab240.banks.Itau.segments.A import SegmentA
from pg_cnab240.banks.Itau.segments.ANF import SegmentANF
from pg_cnab240.banks.Itau.segments.J import SegmentJ, SegmentJFooter, SegmentJHeader
from pg_cnab240.banks.Itau.segments.J52 import SegmentJ52
from pg_cnab240.banks.Itau.payment_status import PaymentStatus


class Itau(Bank):
    def __init__(self):
        super().__init__('Itaú', 'Itau', 341, 13, 1, 'payment_way', payments_status=PaymentStatus)

        # Segment J
        segment_j_types = {
            'slip': '30',
            'other_bank_slip': '31',
        }
        super().set_segment('JHeader', SegmentJHeader, segment_j_types, shipping_only=True)
        super().set_segment('J', SegmentJ, segment_j_types)
        super().set_segment('J52', SegmentJ52, segment_j_types, shipping_only=True)
        super().set_segment('JFooter', SegmentJFooter, segment_j_types, shipping_only=True)

        # Segment A
        super().set_segment('A', SegmentA, {
            'cc': '01',
            'admin_check': '02',
            'doc': '03',
            'poupanca': '05',
            'ccd': '06',
            'docd': '07',
            'normal_darf': '16',
            'simple_darf': '18',
            'gps': '17',
            'city_taxs': '19',
            'darj': '21',
            'gare': '22',
            'ipva': '25',
            'dpvat': '27',
            'billing_title': '30',
            'billing_title_other_bank': '31',
            'fiscal_note': '32',
            'fgts': '35',
            'ted': '41',
            'tedd': '43',
            'gnre': '91',
        })
        super().set_segment('ANF', SegmentANF, {
            'nf': None,
        }, 'A')
    
    def get_file_header(self):
        file_header = FileHeader()
        file_header.set_bank(self)
        return file_header
    
    def get_file_footer(self):
        file_footer = FileFooter()
        file_footer.set_bank(self)
        return file_footer
    
    @staticmethod
    def get_company_document_id(document_type):
        return 2 if document_type == 'cnpj' else 1

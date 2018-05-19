from datetime import datetime
from pg_cnab240.segment_section import SegmentSection


class SlipHeader(SegmentSection):
    def __init__(self, data=None):
        super().__init__('SlipHeader', data, {
            'bank_code': {
                'type': 'int',
                'length': 3,
                'default': 341,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 0,
                'end': 3,
                'value': None,
            },
            'lot_code': {
                'type': 'int',
                'length': 4,
                'default': 0000,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 3,
                'end': 7,
                'value': None,
            },
            'register_type': {
                'type': 'int',
                'length': 1,
                'default': 1,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 7,
                'end': 8,
                'value': None,
            },
            'operation_type': {
                'type': 'string',
                'length': 1,
                'default': 'C',
                'pad_content': ' ',
                'pad_direction': 'left',
                'required': False,
                'start': 8,
                'end': 9,
                'value': None,
            },
            'payment_type': {
                'type': 'int',
                'length': 2,
                'default': 20,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 9,
                'end': 11,
                'value': None,
            },
            'payment_way': {
                'type': 'int',
                'length': 2,
                'default': 41,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 11,
                'end': 13,
                'value': None,
            },
            'lot_layout': {
                'type': 'int',
                'length': 3,
                'default': '030',
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 13,
                'end': 16,
                'value': None,
            },
            'lot_layout_whites': {
                'type': 'whites',
                'length': 1,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'left',
                'required': False,
                'start': 16,
                'end': 17,
                'value': None,
            },
            'company_document_type': {
                'type': 'int',
                'length': 1,
                'default': 2, # 1 = CPF / 2 = CNPJ
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 17,
                'end': 18,
                'value': None,
            },
            'company_document_number': {
                'type': 'int',
                'length': 14,
                'default': '',
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 18,
                'end': 32,
                'value': None,
            },
            'company_document_whites': {
                'type': 'whites',
                'length': 20,
                'default': ' ',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': False,
                'start': 32,
                'end': 52,
                'value': None,
            },
            'agency': {
                'type': 'int',
                'length': 5,
                'default': 0,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 52,
                'end': 57,
                'value': None,
            },
            'agency_whites': {
                'type': 'whites',
                'length': 1,
                'default': ' ',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': False,
                'start': 57,
                'end': 58,
                'value': None,
            },
            'account': {
                'type': 'int',
                'length': 12,
                'default': 0,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 58,
                'end': 70,
                'value': None,
            },
            'account_whites': {
                'type': 'whites',
                'length': 1,
                'default': ' ',
                'pad_content': ' ',
                'pad_direction': 'left',
                'required': False,
                'start': 70,
                'end': 71,
                'value': None,
            },
            'dac': {
                'type': 'int',
                'length': 1,
                'default': 0,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 71,
                'end': 72,
                'value': None,
            },
            'company_name': {
                'type': 'string',
                'length': 30,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': True,
                'start': 72,
                'end': 102,
                'value': None,
            },
            'lot_goal': {
                'type': 'string',
                'length': 30,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': False,
                'start': 102,
                'end': 132,
                'value': None,
            },
            'account_history': {
                'type': 'string',
                'length': 10,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': False,
                'start': 132,
                'end': 142,
                'value': None,
            },
            'company_address_street': {
                'type': 'string',
                'length': 30,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': True,
                'start': 142,
                'end': 172,
                'value': None,
            },
            'company_address_number': {
                'type': 'int',
                'length': 5,
                'default': 0,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 172,
                'end': 177,
                'value': None,
            },
            'company_address_complement': {
                'type': 'string',
                'length': 15,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': False,
                'start': 177,
                'end': 192,
                'value': None,
            },
            'company_address_city': {
                'type': 'string',
                'length': 20,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': True,
                'start': 192,
                'end': 212,
                'value': None,
            },
            'company_address_zipcode': {
                'type': 'int',
                'length': 8,
                'default': 0,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 212,
                'end': 220,
                'value': None,
            },
            'company_address_state': {
                'type': 'string',
                'length': 2,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': True,
                'start': 220,
                'end': 222,
                'value': None,
            },
            'company_address_whites': {
                'type': 'whites',
                'length': 8,
                'default': ' ',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': False,
                'start': 222,
                'end': 230,
                'value': None,
            },
            'occurrences': {
                'type': 'string',
                'length': 10,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': False,
                'start': 230,
                'end': 240,
                'value': None,
            },
        })

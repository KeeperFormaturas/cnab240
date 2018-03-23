from datetime import datetime
from pg_cnab240.file_section import FileSection


class FileFooter(FileSection):
    def __init__(self, data):
        super().__init__('FileFooter', data, {
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
                'default': 9999,
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
                'default': 9,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 7,
                'end': 8,
                'value': None,
            },
            'register_type_whites': {
                'type': 'whites',
                'length': 9,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'left',
                'required': False,
                'start': 8,
                'end': 17,
                'value': None,
            },
            'lots_quantity': {
                'type': 'int',
                'length': 6,
                'default': 1,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 17,
                'end': 23,
                'value': None,
            },
            'registers_quantity': {
                'type': 'int',
                'length': 6,
                'default': 3,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 23,
                'end': 29,
                'value': None,
            },
            'registers_quantity_whites': {
                'type': 'whites',
                'length': 211,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': False,
                'start': 29,
                'end': 240,
                'value': None,
            },
        })
        self.transform_attributes()
        self.associate_data()

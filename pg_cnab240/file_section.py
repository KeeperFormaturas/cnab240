import json
from pg_cnab240.attribute import Attribute


class FileSection:
    def __init__(self, section_name, data, attributes):
        self.section_name = section_name
        self.default_date_format = "%d%m%Y"
        self.default_datetime_format = "%d%m%Y %H%M%S"
        self.default_time_format = "%H%M%S"
        self.data = data
        self.attributes = attributes
    
    def transform_attributes(self):
        for attr, data in self.attributes.items():
            self.attributes[attr] = Attribute(attr, data['type'], data['length'], data['start'], data['end'], data['default'], data['pad_content'], data['pad_direction'], data['required'], self.default_datetime_format, self.default_date_format, self.default_time_format)
    
    def associate_data(self):
        if self.data:
            for name, attr in self.attributes.items():
                if name in self.data:
                    self.attributes[attr].set_value(self.data[name])
                elif attr.is_required():
                    raise Exception('The ' + self.section_name + ' Attribute "' + name + '" is required')
    
    def get_dict(self):
        return self.attributes
    
    def get_json(self):
        return json.dumps(self.get_dict())
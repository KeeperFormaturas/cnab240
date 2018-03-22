class Attribute:
    def __init__(self, name, type, length, start, end, default_value='', pad_content=0, pad_direction='left', required=False, datetime_format='', date_format='', time_format=''):
        self.name = name
        self.type = type
        self.length = length
        self.start = start
        self.end = end
        self.default_value = default_value
        self.pad_content = pad_content
        self.pad_direction = pad_direction
        self.required = required
        self.value = None
    
    def is_required(self):
        return self.required
    
    def set_value(self, new_value):
        if self.type == 'int':
            self.value = new_value
        elif self.type == 'string':
            self.value = str(new_value)
    
    def get_value(self):
        return self.value

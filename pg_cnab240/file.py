class File:
    def __init__(self):
        self.header = None
        self.body = None
        self.footer = None
    
    def verify(self):
        if self.header is None or self.body is None or self.footer is None:
            raise Exception('Header, Body and Footer cannot be None')
        return True

    def generate(self):
        self.verify()
        pass
    
    def read(self, file_content):
        self.verify()
        pass



class Section:
    def __init__(self, attributes=None):
        self.attributes = attributes
    
    def set_attributes(self, attributes):
        self.attributes = attributes
    
    def get_attributes(self):
        return self.attributes
    
    def verify_attributes(self):
        if self.attributes is None:
            raise Exception('Attributes cannot be None')
        return True
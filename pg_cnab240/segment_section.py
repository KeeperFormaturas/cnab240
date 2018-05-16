from pg_cnab240.file_section import FileSection


class SegmentSection(FileSection):
    def __init__(self, section_name, data, attributes, header_class=None, footer_class=None):
        super().__init__(section_name, data, attributes)
        if header_class:
            self.header = header_class()
        if footer_class:
            self.footer = footer_class()
    
    def set_header(self, header):
        self.header = header
        if hasattr(self.header, 'associate_data'):
            self.header.associate_data(self.data)
        
    def set_header_data(self, header_data=dict()):
        if not self.header:
            raise Exception('Header is invalid')
        self.header.associate_data(header_data)
    
    def get_header_line(self):
        self.header.associate_data(self.data)
        return self.header.to_line()
    
    def set_footer(self, footer):
        self.footer = footer
    
    def set_footer_data(self, footer_data=dict()):
        if not self.footer:
            raise Exception('Footer is invalid')
        self.footer.associate_data(footer_data)
    
    def get_footer_line(self):
        self.footer.associate_data(self.data)
        return self.footer.to_line()

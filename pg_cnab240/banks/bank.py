class Bank:
    def __init__(self, name, slug, code):
        self.name = name
        self.slug = slug
        self.code = code
        self.available_segments = dict()
    
    def set_segment(self, segment_name, segment_class, payment_types=dict()):
        self.available_segments[segment_name] = dict(
            segment_name = segment_name,
            segment_class = segment_class,
            payment_types = payment_types,
        )
    
    def get_file_header(self):
        pass
    
    def get_file_footer(self):
        pass

    def get_segment(self, segment):
        pass
    
    def get_payment_segment(self, payment_type):
        for segment_name, segment_dict in self.available_segments.items():
            if payment_type in [*segment_dict['payment_types']]:
                return segment_dict
        raise Exception('Payment Type not Found')

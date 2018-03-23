from pg_cnab240.file_section import FileSection


class SegmentSection(FileSection):
    def __init__(self, section_name, data, attributes):
        super().__init__(section_name, data, attributes)
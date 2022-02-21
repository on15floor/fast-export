def build_filter(args):
    return Filter(args)


class Filter:
    def __init__(self, args):
        self.remove_from_hgignore = ['syntax: glob']
    
    def _clean_hgignore(self, data):
        data = data.split('\n')
        for line in data:
            for el in self.remove_from_hgignore:
                if el not in line:
                    yield line
    
    def file_data_filter(self, file_data):
        if file_data['filename'] == '.hgignore':
            new_data = list(self._clean_hgignore(file_data['data']))
            file_data['filename'] = '.gitignore'
            file_data['data'] = '\n'.join(new_data)

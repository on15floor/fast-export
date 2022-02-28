def build_filter(args):
    return Filter(args)


class Filter:
    def __init__(self, args):
        args = args.split(',')
        self.file = args[0]
        self.bigger_than = 0 if len(args) == 1 else int(args[1])
        
        self.text_extensions = set()
        self.binary_files = set()
        self.directories = set()
    
    def __del__(self):
        with open(self.file, 'w') as f:
            for el in sorted(set(self.finalizing_data())):
                f.write(el + '\n')
    
    def file_data_filter(self, file_data):
        file_name = file_data['filename']
        self.directories.update(self.get_directories(file_name))

        file_ctx = file_data['file_ctx']
        if not file_ctx.islink():
            if file_ctx.isbinary():
                if file_ctx.size > self.bigger_than:
                    self.binary_files.add(file_name)
            else:
                file_ex = self.get_file_extension(file_name)
                self.text_extensions.add(file_ex)

    @staticmethod
    def get_file_extension(file_path):
        file_name = file_path.split('/')[-1]
        ext = file_name.split('.')
        return file_name if len(ext) == 1 else '*.' + ext[-1]
    
    @staticmethod
    def get_file_name(file_path):
        return file_path.split('/')[-1]

    @staticmethod
    def get_directories(file_path):
        return set(file_path.split('/')[:-1])
    
    def finalizing_data(self):
        for _file in self.binary_files:
            ext = self.get_file_extension(_file)
            name = self.get_file_name(_file)
            if ext in self.text_extensions or name in self.directories:
                yield '/' + _file
            else:
                yield ext

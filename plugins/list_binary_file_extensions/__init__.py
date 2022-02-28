def build_filter(args):
    return Filter(args)


class Filter:
    def __init__(self, args):
        args = args.split(',')
        self.file = args[0]
        self.bigger_than = 1024 if len(args) == 1 else int(args[1])
        
        self.text_extensions = set()
        self.binary_files = set()
        self.directories = set()
    
    def __del__(self):
        with open(self.file, 'w') as f:
            for el in sorted(set(self.finalizing_data())):
                f.write(el + '\n')
    
    def file_data_filter(self, file_data):
        self.directories.update(self.get_folders(file_data['filename']))

        file_ctx = file_data['file_ctx']
        if not file_ctx.islink():
            if file_ctx.isbinary():
                if file_ctx.size > self.bigger_than:
                    file_path = file_data['filename']
                    self.binary_files.add(file_path)
            else:
                file_ex = self.get_file_extension(file_data['filename'])
                self.text_extensions.add(file_ex)

    @staticmethod
    def get_file_extension(file_name):
        file_name = file_name.split('/')[-1]
        ext = file_name.split('.')
        return file_name if len(ext) == 1 else '*.' + ext[-1]

    @staticmethod
    def get_folders(file_path):
        return set(file_path.split('/')[:-1])
    
    def finalizing_data(self):
        files_exeptions = set.union(self.text_extensions, self.directories)
        for _file in self.binary_files:
            ext = self.get_file_extension(_file)
            if ext in files_exeptions:
                yield '/' + _file
            else:
                yield ext

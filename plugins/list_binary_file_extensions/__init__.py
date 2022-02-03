def build_filter(args):
    return Filter(args)


class Filter:
    def __init__(self, args):
        self.extensions = set()
        self.file = args
    
    def __del__(self):
        with open(self.file, 'w') as f:
            for ex in sorted(self.extensions):
                f.write(ex + '\n')
    
    def file_data_filter(self, file_data):
        file_ctx = file_data['file_ctx']
        if file_ctx.isbinary() and not file_ctx.islink():
            file_name = file_data['filename'].split('/')[-1]
            ex = file_name.split('.')
            if len(ex) == 1:
                ex = file_name
            else:
                ex = '*.' + ex[-1]
            self.extensions.add(ex)

def build_filter(args):
    return Filter(args)


class Filter:
    def __init__(self, args):
        args = args.split(',')
        self.file = args[0]
        self.bigger_than = 1024 if len(args) == 1 else int(args[1])
        self.extensions = set()
    
    def __del__(self):
        with open(self.file, 'w') as f:
            for ex in sorted(self.extensions):
                f.write(ex + '\n')
    
    def file_data_filter(self, file_data):
        file_ctx = file_data['file_ctx']
        if file_ctx.isbinary() and \
                not file_ctx.islink() and \
                (file_ctx.size() > self.bigger_than):
            file_name = file_data['filename'].split('/')[-1]
            ex = file_name.split('.')
            if len(ex) == 1:
                ex = file_name
            else:
                ex = '*.' + ex[-1]
            self.extensions.add(ex)

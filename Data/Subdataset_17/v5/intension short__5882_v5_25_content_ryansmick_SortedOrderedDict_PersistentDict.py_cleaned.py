from SortedOrderedDict import SortedOrderedDict
class PersistentDict(SortedOrderedDict):
    DEFAULT_DELIM = ": "
    def __init__(self, save_filepath=None, save_delim=DEFAULT_DELIM, compare_fn=None,
                 load_filepath=None, load_delim=DEFAULT_DELIM,
                 load_key_trans_func=None, load_value_trans_func=None):
        super().__init__(compare_fn=compare_fn)
        self.save_filepath = save_filepath
        self.save_delim = save_delim
        if load_filepath:
            self.load(filepath=load_filepath, delim=load_delim,
                      key_trans_func=load_key_trans_func,
                      value_trans_func=load_value_trans_func)
    def save(self, save_filepath=None, delim=None):
        filepath = save_filepath or self.save_filepath
        if not filepath:
            raise ValueError("No save filepath specified. "
                             "Specify it in the constructor or as a parameter to the save method.")
        delim = delim or self.save_delim
        with open(filepath, 'w') as file:
            for key, value in self.iteritems_ordered():
                file.write(f"{key}{delim}{value}\n")
    def load(self, filepath, delim=DEFAULT_DELIM,
             key_trans_func=None, value_trans_func=None,
             add_to_existing=False):
        if not add_to_existing:
            self.clear()
        with open(filepath, 'r') as file:
            for line in file:
                key, value = line.split(delim, 1)
                value = value.rstrip()
                if key_trans_func:
                    key = key_trans_func(key)
                if value_trans_func:
                    value = value_trans_func(value)
                self.insert(key, value)
    def __enter__(self):
        if not self.save_filepath:
            raise ValueError("No save filepath specified.")
        return self
    def __exit__(self, exception_type, exception_value, traceback):
        self.save()
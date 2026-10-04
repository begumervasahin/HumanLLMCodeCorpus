from collections import OrderedDict
class PersistentDict(OrderedDict):
    DEFAULT_DELIM = ": "
    def __init__(self, save_filepath=None, save_delim=DEFAULT_DELIM,
                 load_filepath=None, load_delim=DEFAULT_DELIM,
                 key_transform_func=None, value_transform_func=None):
        super().__init__()
        self.save_filepath = save_filepath
        self.save_delim = save_delim
        if load_filepath:
            self.load(load_filepath, delim=load_delim,
                      key_transform_func=key_transform_func,
                      value_transform_func=value_transform_func)
    def save(self, save_filepath=None, delim=None):
        filepath = save_filepath or self.save_filepath
        if not filepath:
            raise ValueError("A save filepath must be provided either in the constructor or as a parameter to the save method.")
        delim = delim or self.save_delim
        with open(filepath, 'w') as file:
            for key, value in self.items():
                file.write(f"{key}{delim}{value}\n")
    def load(self, filepath, delim=DEFAULT_DELIM,
             key_transform_func=None, value_transform_func=None,
             add_to_existing=False):
        with open(filepath, 'r') as file:
            if not add_to_existing:
                self.clear()
            for line in file:
                key, value = line.split(delim, 1)
                value = value.rstrip()
                if key_transform_func:
                    key = key_transform_func(key)
                if value_transform_func:
                    value = value_transform_func(value)
                self[key] = value
    def __enter__(self):
        if not self.save_filepath:
            raise ValueError("A save filepath must be specified to use PersistentDict in a 'with' statement.")
        return self
    def __exit__(self, exception_type, exception_value, traceback):
        self.save()

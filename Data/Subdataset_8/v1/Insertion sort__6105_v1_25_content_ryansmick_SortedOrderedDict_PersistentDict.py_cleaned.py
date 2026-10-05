from SortedOrderedDict import SortedOrderedDict
class PersistentDict(SortedOrderedDict):
    DEFAULT_DELIM = ": "
    def __init__(self, save_filepath=None, save_delim=DEFAULT_DELIM, compare_fn=None, load_filepath=None, load_delim=': ', load_key_trans_func=None, load_value_trans_func=None):
        super(PersistentDict, self).__init__(compare_fn=compare_fn)
        if load_filepath:
            self.load(load_filepath, delim=load_delim, key_trans_func=load_key_trans_func, value_trans_func=load_value_trans_func)
        self.save_filepath = save_filepath
        self.save_delim = save_delim
    def save(self, save_filepath=None, delim=None):
        if save_filepath:
            filepath = save_filepath
        elif self.save_filepath:
            filepath = self.save_filepath
        else:
            raise ValueError("No save filepath specified. Save filepath must be specified as either constructor parameter or save function parameter")
        if delim:
            current_delim = delim
        else:
            current_delim = self.save_delim
        with open(filepath, 'w+') as f:
            for key, value in self.iteritems_ordered():
                f.write("{}{}{}\n".format(key, current_delim, value))
    def load(self, filepath, delim=': ', key_trans_func=None, value_trans_func=None, add_to_existing=False):
        with open(filepath, 'r') as f:
            if not add_to_existing:
                self.clear()
            for line in f:
                key, value = line.split(delim, 1)
                value = value.rstrip()
                if key_trans_func:
                    key = key_trans_func(key)
                if value_trans_func:
                    value = value_trans_func(value)
                self.insert(key, value)
    def __enter__(self):
        if not self.save_filepath:
            raise ValueError("No save filepath specified")
        return self
    def __exit__(self, exception_type, exception_value, traceback):
        self.save(delim=self.save_delim)
if __name__ == "__main__":
    with PersistentDict(save_filepath="data.txt") as p_dict:
        p_dict["key1"] = "value1"
        p_dict["key2"] = "value2"
        p_dict.save()
    new_p_dict = PersistentDict(load_filepath="data.txt")
    print(new_p_dict)

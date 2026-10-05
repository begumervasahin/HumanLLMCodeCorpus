class PrefixMatcher:
    def __init__(self, options):
        self._options = options
    def match_unique(self, value):
        result = self.match(value)
        if len(result) != 1:
            if len(result) == 0:
                raise Exception(f"'{value}' did not match any options.")
            else:
                raise Exception(f"'{value}' is ambiguous. Please clarify further. Available: {', '.join(sorted(list(result)))}")
        return result[0]
    def match(self, value):
        return [option for option in self._options if option.startswith(value)]
if __name__ == "__main__":
    pm = PrefixMatcher(["import", "install", "foo"])
    print(pm.match("i"))
    print(pm.match_unique("i"))
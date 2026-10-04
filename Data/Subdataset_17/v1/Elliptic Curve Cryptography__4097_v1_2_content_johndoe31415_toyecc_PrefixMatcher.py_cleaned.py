class PrefixMatcher:
    def __init__(self, options):
        self._opts = options
    def matchunique(self, value):
        result = self.match(value)
        if len(result) != 1:
            if len(result) == 0:
                raise Exception(f"'{value}' did not match any options.")
            else:
                raise Exception(f"'{value}' is ambiguous. Please clarify further. Available: {', '.join(sorted(list(result)))}")
        return result[0]
    def match(self, value):
        return [option for option in self._opts if option.startswith(value)]
if __name__ == "__main__":
    pm = PrefixMatcher(["import", "install", "foo"])
    print(pm.match("i"))
    try:
        print(pm.matchunique("i"))
    except Exception as e:
        print(e)
    try:
        print(pm.matchunique("im"))
    except Exception as e:
        print(e)
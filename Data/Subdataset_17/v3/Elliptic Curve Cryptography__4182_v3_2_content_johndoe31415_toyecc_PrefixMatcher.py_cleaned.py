class PrefixMatcher:
    def __init__(self, options):
        self._opts = options
    def matchunique(self, value):
        result = self.match(value)
        if len(result) == 0:
            raise Exception(f"'{value}' did not match any options.")
        elif len(result) > 1:
            raise Exception(f"'{value}' is ambiguous. Please clarify further. Available: {', '.join(sorted(result))}")
        return result[0]
    def match(self, value):
        return [option for option in self._opts if option.startswith(value)]
if __name__ == "__main__":
    options = ["import", "install", "foo"]
    pm = PrefixMatcher(options)
    matches = pm.match("i")
    print("Matches for 'i':", matches)
    try:
        unique_match = pm.matchunique("i")
        print("Unique match for 'i':", unique_match)
    except Exception as e:
        print("Error:", e)
    try:
        unique_match = pm.matchunique("im")
        print("Unique match for 'im':", unique_match)
    except Exception as e:
        print("Error:", e)
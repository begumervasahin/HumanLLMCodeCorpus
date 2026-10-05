class PrefixMatcher:
    def __init__(self, options):
        self._options = options
    def match_unique(self, value):
        matches = self.match(value)
        if len(matches) == 0:
            raise ValueError(f"'{value}' did not match any options.")
        elif len(matches) > 1:
            raise ValueError(f"'{value}' is ambiguous. Please clarify further. Available options: {', '.join(sorted(matches))}")
        return matches[0]
    def match(self, value):
        return [option for option in self._options if option.startswith(value)]
if __name__ == "__main__":
    pm = PrefixMatcher(["import", "install", "foo"])
    print("Matches for 'i':", pm.match("i"))
    print("Unique match for 'i':", pm.match_unique("i"))
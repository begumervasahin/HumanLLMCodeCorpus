class PrefixMatcher:
    def __init__(self, options):
        self.options = options
    def match(self, value):
        return [option for option in self.options if option.startswith(value)]
    def match_unique(self, value):
        matches = self.match(value)
        if len(matches) == 0:
            raise ValueError(f"'{value}' did not match any options.")
        elif len(matches) > 1:
            raise ValueError(f"'{value}' is ambiguous. Please clarify further. Available: {', '.join(sorted(matches))}")
        return matches[0]
if __name__ == "__main__":
    options = ["import", "install", "foo"]
    matcher = PrefixMatcher(options)
    try:
        matches = matcher.match("i")
        print("Matches for 'i':", matches)
    except ValueError as e:
        print("Error:", e)
    try:
        unique_match = matcher.match_unique("i")
        print("Unique match for 'i':", unique_match)
    except ValueError as e:
        print("Error:", e)
    try:
        unique_match = matcher.match_unique("im")
        print("Unique match for 'im':", unique_match)
    except ValueError as e:
        print("Error:", e)
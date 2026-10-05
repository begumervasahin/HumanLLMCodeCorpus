class PrefixMatcher:
    def __init__(self, options):
        self.options = options
    def find_matches(self, prefix):
        return [option for option in self.options if option.startswith(prefix)]
    def match_unique(self, prefix):
        matches = self.find_matches(prefix)
        if len(matches) != 1:
            if len(matches) == 0:
                raise ValueError(f"'{prefix}' did not match any options.")
            else:
                raise ValueError(f"'{prefix}' is ambiguous. Please clarify further. Available: {', '.join(sorted(matches))}")
        return matches[0]
if __name__ == "__main__":
    pm = PrefixMatcher(["import", "install", "foo"])
    print("Matching options for prefix 'i':", pm.find_matches("i"))
    print("Unique match for prefix 'i':", pm.match_unique("i"))
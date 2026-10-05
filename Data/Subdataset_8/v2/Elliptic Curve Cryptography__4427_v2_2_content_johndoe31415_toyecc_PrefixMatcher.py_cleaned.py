class PrefixMatcher:
    def __init__(self, options):
        self._options = options
    def matchunique(self, value):
        matches = self.match(value)
        if len(matches) == 0:
            raise Exception("'%s' did not match any options." % value)
        elif len(matches) > 1:
            raise Exception("'%s' is ambiguous. Please clarify further. Available options: %s" % (value, ", ".join(sorted(matches))))
        return matches[0]
    def match(self, value):
        return [option for option in self._options if option.startswith(value)]
if __name__ == "__main__":
    pm = PrefixMatcher(["import", "install", "foo"])
    print("Matches for 'i':", pm.match("i"))
    print("Unique match for 'i':", pm.matchunique("i"))
class Solution:

    def encode(self, strs):
        # Length-prefix encoding: for each s, append len(s) and a separator, then the string
        # e.g., "3#hey5#there"
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            # read length until '#'
            j = s.find('#', i)
            if j == -1:
                # malformed input
                break
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i+length])
            i += length
        return res
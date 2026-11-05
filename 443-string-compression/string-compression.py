class Solution:
    def compress(self, chars: list[str]) -> int:
        
        prev = chars[0]
        count = 1
        i = 0

        for idx in range(1 , len(chars)):
            if chars[idx] == prev:
                count += 1
            else:
                chars[i] = prev
                i += 1
                if count > 1:
                    val = str(count)
                    if count < 10:
                        chars[i] = val
                        i += 1
                    else:
                        for v in list(val):
                            chars[i] = v
                            i += 1

                prev = chars[idx]
                count = 1

        chars[i] = prev
        i += 1

        if count > 1:
            val = str(count)
            if count < 10:
                chars[i] = val
                i += 1
            else:
                for v in list(val):
                    chars[i] = v
                    i += 1

        return i
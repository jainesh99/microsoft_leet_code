def myAtoi(self, s: str) -> int:
    if len(s.strip()) == 0:
        return 0

    s = s.strip()
    new_str = ""

    if s[0] == "-" or s[0] == "+":
        i = 1
        while i < len(s):
            if s[i].isdigit():
                new_str = new_str + s[i]
            else:
                break
            i += 1
    else:
        i = 0
        while i < len(s):
            if s[i].isdigit():
                new_str = new_str + s[i]
            else:
                break
            i += 1

    if new_str:
        int_value = int(new_str)
        if s[0] == "-":
            int_value = int_value * -1
        if int_value > (2**31 - 1):
            return 2**31 - 1
        if int_value < (-(2**31)):
            return -(2**31)
        return int_value
    else:
        return 0

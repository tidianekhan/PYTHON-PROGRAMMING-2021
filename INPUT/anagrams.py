

def raw_frequency(element):
    d = {}
    for i in element:
        d[i] = d.get(i, 0) + 1
    return d


def is_anagram_of(a, b):
    a = a.strip()
    b = b.strip()
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    a = a.lower()
    b = b.lower()

    if a != b and raw_frequency(a) == raw_frequency(b):
        return True
    else:
        return False


print(is_anagram_of("William Shakespeare", "I am a weakish speller"))

      

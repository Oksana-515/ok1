import re


def remove_special_chars(text):
    return re.sub(r'[^a-zA-Z0-9]', '', text)

def words_with_char(text, char):
    return re.findall(rf'\b\w*{char}\w*\b', text)

def words_of_length(text, n):
    return re.findall(rf'\b\w{{{n}}}\b', text)

def words_a_b_ends_s(text):
    return re.findall(r'\b[a|b]\w*s\b', text, flags=re.IGNORECASE)
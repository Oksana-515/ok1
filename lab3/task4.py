import re

def convert_date_format(date_str):
    # Match yyyy-mm-dd format
    match = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})', date_str)
    if match:
        return f"{match.group(3)}-{match.group(2)}-{match.group(1)}"
    return date_str  # return original if format doesn't match

# Example usage:
print(convert_date_format("2024-02-11"))  # Output: 11-02-2024
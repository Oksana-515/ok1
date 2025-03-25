import re

def clean_python_code(code):
    # Remove single-line comments
    code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
    
    # Remove multi-line comments
    code = re.sub(r'\'\'\'.*?\'\'\'|\"\"\".*?\"\"\"', '', code, flags=re.DOTALL)
    
    # Process lines while preserving single blank lines between blocks
    lines = []
    for line in code.split('\n'):
        stripped = line.rstrip()
        if stripped or (lines and not lines[-1]):  # Keep if non-empty or follows empty
            lines.append(stripped if stripped else '')
    
    # Remove leading/trailing empty lines while preserving internal structure
    return '\n'.join(lines).strip('\n')
import re

def extract_1857_block():
    with open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_13\Dostoevsky.txt', 'r', encoding='utf-8') as infile:
        text = infile.read()
    pattern = r'\n(1857 год[^\n]*\n.*?)(?=\b(?:\d{4})\s*?)'
    
    match = re.search(pattern, text, re.DOTALL)
    
    print(str(match.group(1)))
extract_1857_block()
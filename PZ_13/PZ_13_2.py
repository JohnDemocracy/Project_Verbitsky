import re

def find_all_years():
    with open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_13\Dostoevsky.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    pattern = r'\b\d{4}(?:[–-]\d{4})?\s*(?:год[ау]?|г\.|гг\.?)'
    
    matches = re.findall(pattern, text, re.UNICODE)
    
    for i, year in enumerate(matches, 1):
        print(year)
    
    print(f"Всего элементов: {len(matches)}")
    
    return matches

result = find_all_years()
import re

with open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_13\ips.txt', 'r', encoding='utf-8') as file:
        text = file.read()

pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    
matches = re.findall(pattern, text, re.UNICODE)
    
if matches:
    for i in matches:
        print(i)
else:
    print("No IPs")
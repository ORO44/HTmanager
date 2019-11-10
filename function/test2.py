import re

KK = 'SDFSDF[5]'
num = re.findall(r'\[\d+\]', KK)
print(num)

import re

inputstr = input("")
ans = re.sub('s', 'c',f'{inputstr}')
print(ans)
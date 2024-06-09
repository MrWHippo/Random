import re

inputstr = input("")
ans = re.sub('\d', '*',f'{inputstr}')
print(ans)
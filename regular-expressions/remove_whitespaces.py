import re

inputstr = input("")
ans = re.sub('\s', '',f'{inputstr}')
print(ans)
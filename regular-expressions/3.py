import re 

inputstr = input()

ans = re.sub('[^\d\s]','',f'{inputstr}')
print(ans)
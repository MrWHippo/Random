import re 

inputstr = input()

ans = re.sub('[aeiou]','_',f'{inputstr}')
print(ans)
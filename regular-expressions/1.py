import re

inputstr = input("")
ans = re.sub('[!\s?(){}\[\]\-+\*&\^%$£:;\',\.<>/"_=#~]', '',f'{inputstr}')
print(ans)
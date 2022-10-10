import re
p="tHis Is"
new=re.sub(p,"This is","tHis Is an unc\ rlean e”d string")
print(new)
test_str = ''.join(letter for letter in new if letter.isalnum())
print(test_str)
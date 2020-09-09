#		You have a test string . Your task is to match the pattern xxxAxxxxxxxxxxAxxx
#		Here x denotes any word character and A denotes any non-word character.



Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#		You have a test string . Your task is to match the pattern XXaXXaXX
#		Here, a denotes whitespace characters, and X denotes non-white space characters.


Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#		Given a test string, s , write a RegEx that matches s under the following conditions:

#		1. s must start with Mr., Mrs., Ms., Dr. or Er. .
#		2. The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).



Regex_Pattern = r'^(Mr.)|(Mrs.)|(Dr.)|(Er.).+'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

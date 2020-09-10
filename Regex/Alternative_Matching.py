#		Given a test string, s , write a RegEx that matches s under the following conditions:

#		1. s must start with Mr., Mrs., Ms., Dr. or Er. .
#		2. The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).


#   contains Mr. or Mrs. or Dr. or Er. => (Mr|Mrs|Dr|Er)\.
#   one or more alphabetical letters =>  [a-zA-Z]+
#   rest means last of the string => $
Regex_Pattern = r'^(Mr|Mrs|Dr|Er)\.[a-zA-Z]+$'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

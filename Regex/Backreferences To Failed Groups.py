Task

You have a test string S.
Your task is to write a regex which will match S, with following condition(s):

S consists of 8 digits.
S may have "" separator such that string S gets divided in 4 parts, with each part having exactly two digits. (Eg. 12-34-56-78)

Valid S

12345678
12-34-56-87

Invalid S

1-234-56-78
12-45-7810
-----------------------------------------------------------------------------------------------------------
									#Solution


Regex_Pattern = r"^\d{2}(-?)\d{2}\1\d{2}\1\d{2}$"	# Do not delete 'r'.
# If - is present after 2 digits then it must be present after all 2 digits. And if it is not present after 2 digits then it must not be present in string 
at all.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

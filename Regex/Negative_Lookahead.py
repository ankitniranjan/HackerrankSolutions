#		You have a test String S.
#		Write a regex which can match all characters which are not immediately followed by that same character.



# Any char(.) Not follow(?!) by itself(\1)
# \Number works only on group thus cann't be used  ".(?!\1)"

Regex_Pattern = r"(.)(?!\1)"	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

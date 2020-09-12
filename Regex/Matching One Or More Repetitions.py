#		+
#	The + tool will match one or more repetitions of character/character class/group.
-------------------------------------------------------------------------------

For Example:

w+ : It will match the character w 1 or more times.
[xyz]+ : It will match the character x, y or z 1 or more times.
\d+ : It will match any digit 1 or more times.


-----------------------------------------------------------------------------------------
			# Solution


Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

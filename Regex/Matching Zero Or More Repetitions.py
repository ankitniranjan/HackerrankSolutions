#		*
#	The * tool will match zero or more repetitions of character/character class/group.

-------------------------------------------------------------------------------------------------

For Example:

w* : It will match the character w 0 or more times.
[xyz]* : It will match the characters x, y or z 0 or more times.
\d* : It will match any digit 0 or more times.

--------------------------------------------------------------------------------------------------
				# Solution

Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

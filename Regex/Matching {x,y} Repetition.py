#		{x,y}
#		The {x,y} tool will match between x and y (both inclusive) repetitions of character/character class/group.

#	1.	w{3,5} : It will match the character w , 3,4 or 5 times.
#	2.	[xyz]{5,} : It will match the character x, y or z 5 or more times.
#	3.	\d{1, 4} : It will match any digits 1, 2, 3,4 or more times.

-----------------------------------------------------------------------------------------------------------------


Regex_Pattern = r'^[\d]{1,2}[a-zA-Z]{3,}[.]{0,3}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

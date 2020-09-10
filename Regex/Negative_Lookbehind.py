#		You have a test String S.
#		Write a regex which can match all the occurences of characters which are not immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U).



# not preceded by => (?<![aeiouAEIOU])
# sequence of characters=> .   

Regex_Pattern = r"(?<![aeiouAEIOU])."	    # Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

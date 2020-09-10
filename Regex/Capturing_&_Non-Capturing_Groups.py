#		You have a test String S.
#		Your task is to write a regex which will match  with the following condition:

#		S should have 3 or more consecutive repetitions of ok.


# Any characters 0 or more => .*
# to treat 'ok' as a word we need to group them =>  (ok)
# if we use [ok] then it will be treated 'o' and 'k' separately which means it will match for  .*o.*k.*
# 3 or more times => {3,} the last empty index will be treated as infinity

Regex_Pattern = r'.*(ok){3,}.*'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

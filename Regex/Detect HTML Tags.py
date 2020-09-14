# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys
print(';'.join(sorted(set(re.findall('<(\w+)', sys.stdin.read())))))




=> We need to compile the regex exp only when we are using raw expression => r"____"

sys.stdin.read => reads all the data from the file at one go
regex_expression = '<(\w+)'    => It will matche only starting tags like <a> but not closing tags like </a>
re.findall()	=> It will return all the matches in the form of the list
set()		=> removes duplicates
sorted()	=> sort the tags in alphabetical order
';'.join()		=> join the elements of the list with ';' and make them into a single string

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

lang = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'

lang = lang.replace(':', '|')  					#string manipulation

regex = r'^[1-9]\d{4}\s' + '(' + lang + ')$'		#regex_expression

pattern = re.compile(regex)								#compilation

N = int(input())

for _ in range(N):
    if pattern.match(input()):
        print('VALID')
    else:
        print('INVALID')
		
-------------------------------------------END-------------------------------------------------------		
		
# Don't Use below pattern

#	regex_pattern = re.compile(r"""
#	 ^[0-9]{4}                # For numberic value between 10000-100000 in the beginning(^)
#	 \s						  # For single Whitespace
#	 '('
#		+ lang+			  # For languages
#	 ')'
#	 $                 		  # For ending
#	""", re.VERBOSE)

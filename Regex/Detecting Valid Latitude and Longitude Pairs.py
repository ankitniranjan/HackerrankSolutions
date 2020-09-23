For a valid (latitude, longitude) pair:
-90<=X<=+90 and -180<=Y<=180.

12							Valid
(75, 180)						Valid
(+90.0, -147.45)					Valid
(77.11112223331, 149.99999999)				Valid
(+90, +180)						Valid
(90, 180)						Valid
(-90.00000, -180.0000)					Invalid
(75, 280)						Invalid
(+190.0, -147.45)					Invalid
(77.11112223331, 249.99999999)				Invalid
(+90, +180.2)						Invalid
(90., 180.)						Invalid
(-090.00000, -180.0000)					Invalid
------------------------------------------------------------------------------------------------------------------

import re

n = int(input())

Reg = r"\([+\-]?(90(\.0+)?|[1-8]\d(\.\d+)?|\d(\.\d+)?), [+\-]?(180(\.0+)?|1[0-7]\d(\.\d+)?|\d{2}(\.\d+)?|\d(\.\d+)?)\)"

for _ in range (n):
    p = input()
    print("Valid" if re.match(Reg,p) is not None else "Invalid")
	
----------------------------------------------------------------------------------------------------------------------------


import re

SIGN = '[\+-]?'
DECIMALS = '(\.[0-9]+)?'
ZEROS = '(\.0+)?'

LATITUDE =  f'{SIGN}(90{ZEROS}|[1-8]\d{DECIMALS}|\d{DECIMALS})'		#+/-90.000 | +/-(1-8)\d.873463746 | +/-(0-9).84738738
LONGITUDE = f'{SIGN}(180{ZEROS}|1[0-7]\d{DECIMALS}|[1-9]\d{DECIMALS}|\d{DECIMALS})'	 #+/-180.000 | 1(0-7)\d.847387 | (1-9)\d.48787 | \d.89787

REGEX = f'\({LATITUDE}, {LONGITUDE}\)'
pattern = re.compile(REGEX)

def validate(value):						# f => We can use variables.
    return pattern.search(value)				# r => Everything considers as a string , no special meaning.

for _ in range(int(input())):
    if validate(input()):
        print('Valid')
    else:
        print('Invalid')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r'^(\d{1,3})[-\s](\d{1,3})[-\s](\d{4,10})$'

n = int(input())

for _  in range(n):
    line = input()
    number = re.search(pattern, line)
    print ("CountryCode=" + number.group(1) + ",LocalAreaCode=" + number.group(2) + ",Number=" + number.group(3))

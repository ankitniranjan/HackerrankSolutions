for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(((10 ** i - 1) / 9) * i))
	
# Logic
# 1*1
# 11*2
# 111*3
# 1111*4
# ...

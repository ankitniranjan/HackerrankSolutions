# The main algorithm that keeps track of coordinates 
def spiralSplicer(inp): 
    # Batch size tracker 
    step_count = 1
   
    # Batch size limiter 
    step_limit = 2
   
    # switches between -1 and +1 
    adder = 1
   
    # Co-ordinates of step K 
    x, y = 0, 0
   
    for n in range(2, inp + 1): 
     
        # Keeps track of steps 
        # Checks on the current batch 
        if (step_count <= .5 * step_limit): 
            x += adder # Switch to operating on x 
   
        elif (step_count <= step_limit): 
            y += adder # Switch to operating on x 
           
        if (step_count == step_limit): 
            # Changes adder to -1 and vice versa 
            adder *= -1
   
            # Keeps on updating 'step_limit' 
            step_limit += 2
              
            # Resets count 
            step_count = 0
        step_count += 1
    print (x, y) 
   
def primeIndex(inp): 
    cnt, prime_c = 0, 0
    for i in range(2, 1000000 + 1): 
        cnt = 0
        for j in range(2, i + 1): 
            if (i % j == 0): 
                cnt += 1
          
        if (cnt == 1): 
            prime_c += 1
   
            if (inp == i): 
   
                """ Replaces the prime number with  
                    Step K which will be fed into 
                    the main algorithm """
                inp = prime_c 
                break
    return inp 
   
# driver code 
n = int(input())
for i in range(n):
    inp = int(input())
    # Prime Index Finder Output ported to final algorithm 
    temp = primeIndex(inp) 
    spiralSplicer(temp) 

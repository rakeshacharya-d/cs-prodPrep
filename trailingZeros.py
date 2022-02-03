### Trailing 0s in n! = Count of 5s in prime factors of n! = floor(n/5) + floor(n/25) + floor(n/125) + ... 

def trailingZeroes(self, N):
    	#code here 
    	c=0
    	i=5
    	while(N/i >= 1):
    	    c+= int(N/i)
    	    i*=5
        return c


import time 

n = 50

while n > 0 : 
    print("\rFlight 1 will leave in {} minutes".format(n),end=" ")
    n -= 10
    time.sleep(1)
print("\nflight has dperated")
#example 2 without threads

import time

def sleeper(n, i):
    print ('Hi, I am function {}. Going to sleep for 5 seconds \n'.format(i))
    time.sleep(n)
    print('function{} has woken up from sleep \n'.format(i))




start = time.time()

for i in range(5):
    print('{} has started \n'.format(i))
    x = sleeper(5, i)
    
    
end  = time.time()


print('time taken: {}'.format(end - start))
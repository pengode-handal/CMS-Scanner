import time
import sys
from count import count
done = True
#here is the animation



count = 0
while done:
        count = count + 1
        sys.stdout.write(f'{count}\n')
        time.sleep(1)
        if count == 10:
            exit()




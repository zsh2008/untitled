# clockdeco_demo.py

import time
from clockdeco import clock

@clock
def snooze(sec):
    time.sleep(sec)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__ == "__main__":
    print '*'*40, 'Calling snooze(123)'
    snooze(12)
    print '*'*40, 'Calling factorial(6)'
    print '6! =', factorial(6)

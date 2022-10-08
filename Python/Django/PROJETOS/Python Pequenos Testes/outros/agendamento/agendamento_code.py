import sched
import time 
from datetime import datetime, timedelta

scheduler = sched.scheduler(time.time, time.sleep)

def soma(n1, n2):
    print(f'Soma: {n1+n2} Tempo: {time.ctime()}')
    scheduler.enter(2, 1, soma, (2, 2))
    
def sub(n1, n2):
    print(f'Sub: {n1-n2} Tempo: {time.ctime()}')
    scheduler.enter(2, 1, sub, (2, 2))

def sche():
    scheduler.enter(5, 1, soma, (2, 2))
    scheduler.enter(5, 1, sub, (2, 2))

sche()
scheduler.run()
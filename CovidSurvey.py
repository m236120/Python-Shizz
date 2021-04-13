#Simple program to help fill out the morning survey.
#Will be useless soon, but could be good proof-of-concept.

import time
import random
from pynput.keyboard import Key, Controller

arr = [Key.tab,Key.tab,"13",Key.tab,"Sturdifen",Key.tab,"Dale",Key.tab,Key.down,Key.tab,Key.enter,1,Key.tab,Key.tab,Key.right,Key.tab,Key.right,Key.tab,Key.right,Key.tab,Key.right,Key.tab,Key.right,Key.tab,Key.right,Key.tab,Key.right,Key.tab,Key.right,Key.tab,Key.down,Key.tab,Key.down,Key.tab,Key.tab,Key.enter,1,Key.tab,Key.tab,Key.tab,Key.tab,];
print("Waiting.");
time.sleep(1);
print("Waiting..");
time.sleep(1);
print("Waiting...");
time.sleep(1);

keyboard = Controller();

print("Started!");
for e in arr:
    if isinstance(e, str):
        keyboard.type(e);
    elif isinstance(e, float) or isinstance(e, int):
        time.sleep(e);
    else:
        keyboard.press(e);
        keyboard.release(e);
    delay = random.uniform(0.1, .4);
    time.sleep(delay);
print("Done.");

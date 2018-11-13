import math
import time
import webbrowser as web

link = "http://www.vg.no/"

count = 0
reps = 0


while True:
    if count < reps:
        time.sleep(2)
        web.open_new_tab(link)
        count += 1
    else:
        print("Goodbye!\n")
        break

print("Hello again!")

# Prime number checker

y = 3
x = y // 2

while x > 1:
    if y  % x == 0:
        print(y, "has a factor", x)
        break
    x -= 1
else:
    print(y, "is a prime number")
import time
import webbrowser as web

linktoopen = input("What link shall I open? ")
secs = int(input("How often in minutes shall I open the link? ")) * 60
countin = int(input("How many times shall I repeat? "))
count = 0

while count < countin:
    time.sleep(secs)
    web.open_new_tab(linktoopen)
    count += 1

print("Productivity alarm finished. Please restart to use again :)")

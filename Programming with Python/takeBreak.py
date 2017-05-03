# 1. Use functions
# Take a break mini project

import time
import webbrowser

total_breaks = 3
break_count = 0

while(break_count < total_breaks) :
    print("The program started on " + time.ctime())
    time.sleep(10)
    webbrowser.open("http://www.google.com")
    break_count = break_count + 1
    

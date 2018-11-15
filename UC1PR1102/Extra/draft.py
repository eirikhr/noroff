import sys

if sys.platform.startswith('win32'):
    print("Youre a windows guy")
elif sys.platform.startswith('linux'):
    print("Youre a linux guy")

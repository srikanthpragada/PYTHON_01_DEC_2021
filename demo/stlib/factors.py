# Take a number on command line and display its factors
import sys

if len(sys.argv) < 2:
    print("Usage : python factors.py number")
    exit(0)

num = int(sys.argv[1])     # First command line argument

for i in range(2, num//2 + 1):
    if num % i == 0:
        print(i)


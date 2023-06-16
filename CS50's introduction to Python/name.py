import sys

# try:
#     print('hello, ', sys.argv[1])
#     print("hello, my name is ", sys.argv[1])
# except IndexError:
#     print('too few arguments')

if len(sys.argv) < 2:
    sys.exit('too few arguments')
elif len(sys.argv) > 2:
    sys.exit('too many arguments')

print('hello, ', sys.argv[1])
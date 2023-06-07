# try:
#         x = int(input("What's x?\n"))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         print(f"x is {x}")

# while True:
#     try:
#         x = int(input("What's x?\n"))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")

# while True:
#     try:
#         x = int(input("What's x?\n"))
#         break
#     except ValueError:
#         print("x is not an integer")

def main():
    x = get_int("What's x?\n")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")

main()
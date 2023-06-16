
def main():
    hello("world")
    goodpye("world")

def hello(name):
    print(f'hello, {name}')

def goodpye(name):
    print(f"goodbye, {name}")
# print(__name__)
if __name__ == '__main__':
    main()
import sys
import argparse

parser = argparse.ArgumentParser(description="Prints meow n times") # 可以在命令行中输入 python meows.py -h 查看帮助信息
parser.add_argument("-n", help="Number of times to print meow", default=1, type=int) # -n 是參數，預設值是 1，型態是 int，透過 args.n 取得
args = parser.parse_args()

for _ in range(args.n):
    print("meow") 
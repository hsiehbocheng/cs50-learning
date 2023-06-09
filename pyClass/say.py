import cowsay
import sys
from saving import hello

print(__name__)
if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
    hello(sys.argv[1])
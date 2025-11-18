import sys

from shop import OrderPayment

if __name__ == '__main__':
    sys.setrecursionlimit(60)
    OrderPayment.LoadOptions.load_options()

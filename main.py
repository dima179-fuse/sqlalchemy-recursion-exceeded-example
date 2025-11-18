from sqlalchemy.orm import selectinload

from shop import Order


if __name__ == '__main__':
    Order.LoadOptions.load_options()

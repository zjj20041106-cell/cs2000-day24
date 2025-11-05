
def add_shipping(order_amt: float) -> float:
    """ adds 4 for orders <= 10 (but non-zero), 8 for orders < 30, 12 for larger orders """
    if order_amt == 0:
        return 0
    elif order_amt <= 10:
        return order_amt + 4
    elif order_amt < 30:
        return order_amt + 8
    else:
        return order_amt + 12
# Testing -- we'll come back to this

def is_valid_amount(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
import logging
# DEBUG INFO WARNING ERROR CRITICAL

# logging.basicConfig(level=logging.CRITICAL)
# logging.info("Informative log")
# logging.critical("Critical log")
# logging.warning("Warning log")

logging.basicConfig(level=logging.INFO)

def divide(a, b):
    logging.info("Dividing %d by %d", a, b)

    if b == 0:
        logging.error("Division by zero")
        return

    return a / b

print(divide(10, 2))
print(divide(10, 0))
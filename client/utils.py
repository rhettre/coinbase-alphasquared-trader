import logging
from decimal import Decimal

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with a specified name and level.

    :param name: Name of the logger
    :param level: Logging level (default: logging.INFO)
    :return: Configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    return logger

def round_down(value: Decimal, decimals: int) -> Decimal:
    """
    Round down a Decimal value to a specified number of decimal places.

    :param value: The value to round down
    :param decimals: The number of decimal places to round to
    :return: Rounded down Decimal value
    """
    factor = Decimal(10) ** decimals
    return (value * factor).to_integral_value(rounding='ROUND_DOWN') / factor
import logging


def handler(input: dict, context: object) -> dict[str, any]:
    logging.error('no usermodule found')
    return

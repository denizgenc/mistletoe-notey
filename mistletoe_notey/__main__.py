"""
Make mistletoe_notey runnable as a script with default settings.
"""

import sys
from mistletoe_notey import cli


def main():
    """
    Entry point.
    """
    cli.main(sys.argv[1:])


if __name__ == "__main__":
    main()

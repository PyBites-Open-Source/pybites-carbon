import sys

from . import __version__
from .cli import get_args, get_code
from .carbon import create_code_image


def main():
    args = get_args()
    if args.version:
        print(__version__)
        sys.exit(0)

    code = get_code(args)
    options = {
        "language": args.language,
        "background": args.background,
        "theme": args.theme,
        "interactive": args.interactive,
        "destination": args.destination,
    }
    create_code_image(code, **options)


if __name__ == "__main__":
    main()

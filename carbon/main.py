from .cli import get_args, get_code
from .carbon import create_code_image


def main():
    args = get_args()
    code = get_code(args)
    create_code_image(code, args.language, headless=not args.browser)


if __name__ == "__main__":
    main()

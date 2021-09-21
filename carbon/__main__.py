from .carbon import create_code_image
from .cli import get_args


def main():
    args = get_args()
    options = {
        "language": args.language,
        "background": args.background,
        "theme": args.theme,
        "interactive": args.interactive,
        "destination": args.destination,
        "driver_path": args.driver_path,
    }
    create_code_image(args.code, **options)


if __name__ == "__main__":
    main()

import argparse

import pyperclip


def get_args():
    parser = argparse.ArgumentParser(description="Create a carbon code image")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", type=str, help="File with code")
    group.add_argument(
        "-c", "--clipboard", action="store_true", help="Use code on clipboard"
    )
    group.add_argument("-s", "--snippet", type=str, help="Code snippet")
    parser.add_argument(
        "-l", "--language", type=str, default="python", help="Programming language"
    )
    parser.add_argument(
        "-b",
        "--browser",
        action="store_true",
        default=False,
        help="Run Selenium in interactive (not headless) mode",
    )
    return parser.parse_args()


def get_code(args: argparse.Namespace) -> str:
    """
    Argparse's add_mutually_exclusive_group already guaranteers
    we get one of clipboard, file or snippet
    """
    if args.clipboard:
        code = pyperclip.paste()
    elif args.file:
        with open(args.file) as f:
            code = f.read()
    else:
        code = args.snippet

    return code

import argparse
import os

import pyperclip


def get_args():
    parser = argparse.ArgumentParser(description="Create a carbon code image")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", type=str, help="File with code")
    group.add_argument(
        "-c", "--clipboard", action="store_true", help="Use code on clipboard"
    )
    group.add_argument("-s", "--snippet", type=str, help="Code snippet")
    group.add_argument(
        "-v", "--version", action="store_true", default=False, help="Show version"
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        default=False,
        help="Run Selenium in interactive (not headless) mode",
    )
    parser.add_argument("-l", "--language", type=str, help="Programming language")
    parser.add_argument("-b", "--background", type=str, help="Background color")
    parser.add_argument("-t", "--theme", type=str, help="Name of the theme")
    parser.add_argument(
        "-d",
        "--destination",
        type=str,
        default=os.getcwd(),
        help="Specify folder where image should be stored (defaults to current directory)",
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

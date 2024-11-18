# Pybites Carbon

A small utility to generate beautiful code images using [the awesome _carbon_ service](https://carbon.now.sh/).

## Install Package

### Install as a Standalone Tool using `uv tool` (Recommended)
The [uv package manager](https://docs.astral.sh/uv/) is a "fast Python package and project manager."

You can add the package to [uv tools](https://docs.astral.sh/uv/guides/tools/).

When using playwright, you must also download the browser binary. This package specifically uses the chromium browser.

```shell
# Add package to your tools
uv tool add pybites-carbon

# Install playwright
uv tool run playwright install chromium
# Another way to install playwright. 'uvx' is a alias for 'uv tool run'
uvx playwright install chromium

# To use pybites-carbon as a tool, run it with the command below using the '--from' option
# because it clashes with another PyPI package called 'carbon'
uv tool run --from pybites-carbon carbon

# Run using the 'uvx' alias
uvx --from pybites-carbon carbon
```

### Install as a Project Dependency using uv Package Manager

If you already have a virtual environment and pyproject.toml file set up, ignore the first two steps.

```shell
# Create a new virtual environment
uv venv

# Create a new project
uv init

# Install package as project dependency
uv add pybites-carbon
# Install playwright browser
uv run playwright install chromium
```

### Install with pip

Install from PyPI using pip.

```shell
# Create a new virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate

# Install packages
pip install pybites-carbon
playwright install chromium
```

## Usage

You can load in code from a file, the clipboard or a snippet. You can change the language, the image background and theme. You can also provide a different directory to store the image.

```
$ carbon -h
usage: carbon [-h] [-v] (-f CODE | -c | -s CODE) [-i] [-l LANGUAGE] [-b BACKGROUND] [-t THEME] [-d DESTINATION] [-w WT]
              [--driver-path DRIVER_PATH]

Create a carbon code image

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -f CODE, --file CODE  File with code (default: None)
  -c, --clipboard       Use code on clipboard (default: None)
  -s CODE, --snippet CODE
                        Code snippet (default: None)
  -l LANGUAGE, --language LANGUAGE
                        Programming language (default: python)
  -b BACKGROUND, --background BACKGROUND
                        Background color (default: #ABB8C3)
  -t THEME, --theme THEME
                        Name of the theme (default: seti)
  -d DESTINATION, --destination DESTINATION
                        Specify folder where image should be stored (defaults to current directory) (default:
                        /Users/bbelderbos/code/pybites-carbon)
  -w WT, --wt WT        Windows control theme (default: sharp)
```

## Examples

1. Make a hello world snippet carbon image:

	```
	$ carbon -s 'print("hello world")'
	```

	Resulting image:

	![image from string](https://pybites-tips.s3.eu-central-1.amazonaws.com/pybites-carbon-example1.png)

2. Make a code image of a file, let's pick a [FastAPI](https://fastapi.tiangolo.com/) app I am working on:

	```
	$ cat $HOME/code/infinite-scroll/main.py
	from fastapi import FastAPI, Query
	from sqlmodel import select, Session

	from youtube.models import YouTube, YouTubeRead
	from youtube.db import engine

	app = FastAPI()


	@app.get("/videos/", response_model=list[YouTubeRead])
	def read_videos(offset: int = 0, limit: int = Query(default=100, lte=100)):
		with Session(engine) as session:
			videos = session.exec(
				select(YouTube).offset(offset).limit(limit)
			).all()
			return videos
	```

	Run the script with the `-f` option:

	```
	carbon -f $HOME/code/infinite-scroll/main.py
	```

	Resulting image:

	![image from file](https://pybites-tips.s3.eu-central-1.amazonaws.com/pybites-carbon-example2.png)

3. Copying the following lines to the clipboard:

	Here is my favorite feature: make an image from code I currently have on my OS clipboard (thanks [`pyperclip`](https://pypi.org/project/pyperclip/)):

	Try it out, copy this code:

	```
	from time import sleep

	sleep(2)
	```

	Then run the script with `-c`:

	```
	$ carbon -c
	```

	Resulting image:

	![image from clipboard](https://pybites-tips.s3.eu-central-1.amazonaws.com/pybites-carbon-example3.png)

## Useful shell aliases

I added this alias to my `.zshrc` to make it even easier:

![image from string](https://pybites-tips.s3.eu-central-1.amazonaws.com/pybites-carbon-shell-alias.png)

(Actually I created this image having this alias line on my clipboard, then I ran: `carbon -c -l application/x-sh -t monokai -b #D7D7BE -d $HOME/Downloads`)

## Developer setup

### Installation
1. Clone or fork this repository

2. Install packages using the following options.
	- Install using the uv package manager (recommended).

		`uv sync` also creates project virtual environment if it doesn't exist.
		```shell
		uv sync
		uv playwright install chromium
		```
	- Install using pip.

		Create a virtual environment and install packages using the requirements-dev.txt file.
		```shell
		python -m venv .venv
		pip install requirements-dev.txt
		playwright install chromium
		```
	- Install using the Makefile via `make setup`.

3. Install Tesseract.

	Refer to their [instructions on the GitHub repo](https://github.com/tesseract-ocr/tesseract#installing-tesseract) or the [documentation](https://tesseract-ocr.github.io/tessdoc/Installation.html) for details.

	- Install on Ubuntu with:
		```
		sudo apt install tesseract-ocr
		```

	- Install on Windows following the [Mannheim University Library wiki](https://github.com/UB-Mannheim/tesseract/wiki).

### Running pybites-carbon
The resulting `carbon_image.png` image will be downloaded to your current directory unless you specify a different destination directory using `-d` (or `--destination`).

To run the tests, type `pytest` or `make test` (it uses `pytesseract` - in the dev requirements - to read the text from the generated carbon image file).

We recommend running [`ruff`](https://docs.astral.sh/ruff/) before committing code. To set this up, run this after checking out the repo:

```
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

---

Enjoy and feel free to mention [me](https://twitter.com/bbelderbos) or [Pybites](https://twitter.com/pybites) when you post one of the created images on Twitter.

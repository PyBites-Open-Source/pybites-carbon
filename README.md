# Pybites Carbon

A small utility to generate beautiful code images using [the awesome _carbon_ service](https://carbon.now.sh/).

## Install

### Install with pip
Install from PyPI with pip.
When using playwright, you must also download the browser binary. This package uses the chromium browser.

```shell
pip install pybites-carbon

playwright install
# or only install chromium driver
playwright install chromium
```

### Install using uv package manager

```shell
uv add pybites-carbon
# or add as a dev dependency
uv add --dev pybites-carbon


uv run playwright install
# or only install chromium driver
uv run playwright install chromium
```

### Install as a uv tool
You can add the package to your `uv tool`

```shell
uv tool add pybites-carbon

# But to use pybites-carbon as a tool, you should run it with the command below
# because it clashes with another PyPI package called 'carbon'
uv tool run --from pybites-carbon carbon
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
  --driver-path DRIVER_PATH
                        Path to the executable, if it is not given it reads value from environment variable
                        (DRIVER_PATH) (default: /Users/bbelderbos/bin/chromedriver)
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

1. Create virtual environment
2. Install packages from the following options.
	- Install with pip via `pip install requirements-dev.txt`.
	- Install with Makefile by running `make setup`.
	- Install with the [uv package manager](https://docs.astral.sh/uv/) by installing uv and then running `uv sync`.
3. Download and install browser binaries with playwright. You just need to download the chromium driver.

	```shell
	playwright install chromium

	# if you're using uv package manager
	uv playwright install chromium
	```

4. Install Tesseract. Refer to their [instructions](https://github.com/tesseract-ocr/tesseract#installing-tesseract) for details or install on Ubuntu with:
	```
	sudo apt install tesseract-ocr
	```

The resulting `carbon_image.png` image will be downloaded to your current directory unless you specify a different destination directory using `-d` (or `--destination`).

To run the tests, type `pytest` or `make test` (it uses `pytesseract` - in the dev requirements - to read the text from the generated carbon image file).

We recommend running [`ruff`](https://docs.astral.sh/ruff/) before committing code. To set this up run this after checking out the repo:

```
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

---

Enjoy and feel free to mention [me](https://twitter.com/bbelderbos) or [Pybites](https://twitter.com/pybites) when you post one of the created images on Twitter.

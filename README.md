# Carbon Selenium

A small utility to generate beautiful code images using [the awesome _carbon_ service](https://carbon.now.sh/).

You can load in code from a file, the clipboard or a snippet:

```
$ python script.py -h
usage: script.py [-h] (-f FILE | -c | -s SNIPPET) [-l LANGUAGE] [-b]

Create a carbon code image

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File with code
  -c, --clipboard       Use code on clipboard
  -s SNIPPET, --snippet SNIPPET
                        Code snippet
  -l LANGUAGE, --language LANGUAGE
                        Code string
  -b, --browser         Run Selenium in interactive (not headless) mode
```

Note that these are mutually exclusive:

```
$ python script.py -c -f script.py
usage: script.py [-h] (-f FILE | -c | -s SNIPPET) [-l LANGUAGE] [-b]
script.py: error: argument -f/--file: not allowed with argument -c/--clipboard
```

Examples:

1. Make a hello world snippet carbon image:

```
$ python script.py -s 'print("hello world")'
```

Resulting image:

![image from string](assets/image-from-string.png)

2. Make a code image of a file, let's pick a FastAPI app I am working on:

```
python script.py -f /Users/bbelderbos/code/infinite-scroll/main.py
```

Resulting image:

![image from file](assets/image-from-file.png)

3. Copying the following lines to the clipboard:

Here is my favorite feature: make an image from code I have currently on my OS clipboard (thanks `pyperclip`):

Try it out, copy this code:

```
from time import sleep

sleep(2)
```

Then run the script with `-c`:

```
$ python script.py -c
```

Resulting image:

![image from clipboard](assets/image-from-clipboard.png)

## Setup

Make a virtual environment and install the `requirements.txt` file.

Download the [ChromeDriver](https://chromedriver.chromium.org/), and extract it in a folder, then set it's full path in `.env`, for example:

```
echo "CHROMEDRIVER_PATH=/Users/bbelderbos/bin/chromedriver" > .env
```

The script uses Selenium in headless mode, the resulting `carbon.png` will be downloaded to the folder you run the script from.

---

Enjoy and feel free to mention [me](https://twitter.com/bbelderbos) or [PyBites](https://twitter.com/pybites) when you post one of the created images on Twitter. Also make sure you follow us to receive multiple Python tips every week (using these images).

Future plans / TODOs:

- Create YouTube training video about the code (`selenium` and `argparse`).

- Support passing other font types and background colors so we can also use it for [PyBites Career and Mindset tips](https://codechalleng.es/tips).

- Build an API service around this.

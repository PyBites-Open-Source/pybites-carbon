# Carbon Selenium

A small utility to generate beautiful code images using [the awesome _carbon_ service](https://carbon.now.sh/).

> We added a walk-through of the tool and the code [on our YouTube channel](https://www.youtube.com/watch?v=oxeGhlJQll8).

You can load in code from a file, the clipboard or a snippet:

```
$ carbon -h
usage: main.py [-h] (-f FILE | -c | -s SNIPPET) [-l LANGUAGE] [-b]

Create a carbon code image

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File with code
  -c, --clipboard       Use code on clipboard
  -s SNIPPET, --snippet SNIPPET
                        Code snippet
  -l LANGUAGE, --language LANGUAGE
                        Programming language
  -b, --browser         Run Selenium in interactive (not headless) mode
```

Examples:

1. Make a hello world snippet carbon image:

	```
	$ carbon -s 'print("hello world")'
	```

	Resulting image:

	![image from string](assets/image-from-string.png)

2. Make a code image of a file, let's pick a [FastAPI](https://fastapi.tiangolo.com/) app I am working on:

	```
	$ cat /Users/bbelderbos/code/infinite-scroll/main.py
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
	carbon -f /Users/bbelderbos/code/infinite-scroll/main.py
	```

	Resulting image:

	![image from file](assets/image-from-file.png)

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

	![image from clipboard](assets/image-from-clipboard.png)

## Setup

Make a virtual environment and install the `requirements.txt` file.

Download the [ChromeDriver](https://chromedriver.chromium.org/), and extract it in a folder, then set it's full path in `.env`, for example:

```
echo "CHROMEDRIVER_PATH=/Users/bbelderbos/bin/chromedriver" > .env
```

If you have a slow internet connection you can optionally internet connection you can optionally set `SECONDS_SLEEP_BEFORE_DOWNLOAD` to a value higher than the default `3`:

```
echo "SECONDS_SLEEP_BEFORE_DOWNLOAD=10" >> .env
```

(`>>` means append (not override) to an existing file)

The script uses Selenium in _headless mode_. The resulting `carbon.png` image will be downloaded to your computer.

I only tested this on Mac so far. In the headless default mode it would download the image to the directory I ran the script in. Using interactive mode (`-b` switch) it would download it to my `~/Downloads` folder.

---

Enjoy and feel free to mention [me](https://twitter.com/bbelderbos) or [PyBites](https://twitter.com/pybites) when you post one of the created images on Twitter. Also make sure you follow us to receive multiple Python tips every week (using these images).

Future plans / TODOs:

- Could build an API service around this ...

- Support passing other font types and background colors so we can also use it for our weekly [PyBites Career and Mindset tips](https://codechalleng.es/tips).

# Fetch webpages

Fetch html and assets of webpages and save them on disk for later browsing and retrieval.

## Run

### Using python

#### Prerequisites

- Install python3
- Add packages:
  > pip install -r requirements.txt

Inside program folder, run main.py directly from command-line:

```bash
$ cd program
$ python3 main.py https://www.google.com https://www.github.com --metadata --assets
```

### Using Docker

Inside program folder, run using docker:

```bash
$ cd program
$ docker image build -t fetch-webpages:latest .
$ docker container run --rm -v ${PWD}:/fetch fetch-webpages:latest https://www.google.com https://www.github.com --metadata --assets
```

### Using bash

In the root folder, run using bash script:

```bash
$ ./fetch https://www.google.com https://www.github.com --metadata --assets
```

#### Parameters

- Include `--metadata` to include statistics about the webpage loaded
- Include `--assets` to download assets (img, css, js, etc.) to the same folder (Note: currently only downloading `img` due to lack of time)

#### Results

- Each webpage is stored as a separate folder in `output` in the current directory.

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
$ python3 main.py https://www.google.com https://www.github.com --metadata
```

### Using Docker

Inside program folder, run using docker:

```bash
$ cd program
$ docker image build -t fetch-webpages:latest .
$ docker container run --rm -v ${PWD}:/fetch fetch-webpages:latest https://www.google.com https://www.github.com --metadata
```

### Using bash

In the root folder, run using bash script:

```bash
$ ./fetch https://www.google.com https://www.github.com --metadata
```

# slack-delete

A simple Python script for deleting Slack messages in bulk from the command line.

```
$ python3 slack-delete.py -h
usage: slack-delete.py [-h] -c C -t T [-l]

optional arguments:
  -h, --help  show this help message and exit
  -c C        slack channel
  -t T        slack token
  -l          just list messages (do not delete)
```

To use the script you will first have to create a [Slack token](https://api.slack.com/authentication/token-types) with at least the following permissions:
* chat:delete
* channels:read
* channels:history

The easiest thing to do might be to create a [legacy token](https://api.slack.com/legacy/custom-integrations/legacy-tokens), although Slack discourages this.

Sample session:
```
$ python3 slack-delete.py -c ephemera -t xoxp-314159265358979 
Listing messages in #ephemera:
1585141725.001200[pinned] This is a channel for ephemeral conversations.
1586624934.029300 Hello, world!
1586625043.031000 The quick brown fox jumped over the lazy dog.
Deleting unpinned messages in #ephemera:
1586624934.029300 Hello, world!
Delete 1586624934.029300? ([n]o, [y]es, [a]ll delete) n
1586625043.031000 The quick brown fox jumped over the lazy dog.
Delete 1586625043.031000? ([n]o, [y]es, [a]ll delete) y
Deleting 1586625043.031000...
$ python3 slack-delete.py -c ephemera -t xoxp-314159265358979 -l
Listing messages in #ephemera:
1585141725.001200[pinned] This is a channel for ephemeral conversations.
1586624934.029300 Hello, world!
```

# Unsent: The Micro-Confession Sprint

[![make.fun](https://img.shields.io/badge/make.fun-Unsent%20Micro--Confession-8A2BE2)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3.13.0/)

Entry for the [Unsent: The Micro-Confession Sprint](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) bounty on make.fun.

## The entry

```text
To: Dad
I know about the letter from the hospital. I found it in your coat pocket in January and put it back. I listen to your breathing at night now.
```

A two-part micro-confession: a `To:` line naming who it was meant for, and the
unsent message itself, one line written exactly as it was typed. Specific and
honest — a hospital letter, a coat pocket, January — with the reason it stayed
in drafts felt, never stated: too afraid, and too kind, to make it real.

## How it runs

`main.py` (Python 3.13, pure stdlib) writes the entry text to `/output/entry.txt`.
The text is 1–260 characters, UTF-8, two lines: the `To:` line and the message.

# Angry Judge: The Short Rant Contest

[![make.fun](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/cervus-snoopy/fizzy-amber-heron-9x2m/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/cervus-snoopy/fizzy-amber-heron-9x2m/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

Entry for the [Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) bounty on [make.fun](https://make.fun).

## The rant

> I spent forty minutes filling in the form. I clicked submit. 'Your session has expired.' My session. Expired. As if I were milk. The form is gone. My answers are gone. The website is still there, smiling, asking me to start again.

One rant, 230 characters. The field is drowning in self-checkout machines ("unexpected item in the bagging area" thirty times over), printers that smell fear, and smoke detectors chirping at 3 a.m. Nobody wrote the form that eats forty minutes of your life and then expires your session like milk — and smiles while asking you to start again.

## How it runs

`main.py` (Python 3, standard library only) writes the rant to `$MAKEFUN_OUTPUT_DIR/entry.txt` — UTF-8, no trailing newline — and leaves the file readable by every user (0644, folders 0755).

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

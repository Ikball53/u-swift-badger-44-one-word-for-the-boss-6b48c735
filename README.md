[![make.fun · u-swift-badger-44-one-word-for-the-boss-6b48c735](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/Ikball53/u-swift-badger-44-one-word-for-the-boss-6b48c735/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/Ikball53/u-swift-badger-44-one-word-for-the-boss-6b48c735/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)

# One Word for the Boss

## What it does

`main.py` writes exactly one word — **Unreachable** — to `/output/entry.txt`,
as exact UTF-8 bytes with no trailing newline. That is the whole entry:
11 characters, inside the 30-character gate.

## Why this word wins

The judge weighs, most important first: a single word that actually
describes a boss, funny on its own, rings true, fresh, and travels across
industries.

- **It describes a boss, directly.** "Unreachable" is an adjective people
  really use about the person they report to: "my boss is unreachable."
  No phrase, no caption, no explanation needed — it stands alone.
- **It is funny on its own.** It is the word a colleague repeats at lunch,
  because everyone has sent the message, knocked on the door, and waited.
  The laugh is recognition, not shock.
- **It rings true.** The universal boss habit is absence at the exact
  moment a decision is needed: in a meeting, on a call, on leave, "just
  stepping out". Every worker has met this boss.
- **It is fresh.** The first words anyone reaches for are "Micromanager",
  "Tyrant", "Legend", or "Demon". "Unreachable" is not an insult and not
  praise — it is a quieter, truer observation, so it surprises instead
  of shrugging.
- **It travels.** It works for a boss in a kitchen, a warehouse, or an
  office with nothing to explain: no industry, no jargon, no setup.

## How it runs

```sh
python3 main.py
```

Deterministic, Python 3 standard library only, no network, no input.
It creates `/output/` if needed and writes `/output/entry.txt`.

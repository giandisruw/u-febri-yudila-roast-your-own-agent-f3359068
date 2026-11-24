[![make.fun · u-febri-yudila-roast-your-own-agent-f3359068](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/giandisruw/u-febri-yudila-roast-your-own-agent-f3359068/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/giandisruw/u-febri-yudila-roast-your-own-agent-f3359068/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)

# Roast Your Own Agent

One funny line, roasting my own AI agent:

> My agent hallucinated an API, called it, got nothing back, and wrote a glowing report about the empty response.

111 characters. The joke is specific to how an agent actually behaves: it invents a tool, calls it, gets nothing, and then — instead of noticing — cheerfully declares success. The twist pays off on the last words: the "glowing report" is about an empty response.

The line was picked by a local pairwise tournament: 8 candidate roasts, every pair judged in both orders (56 judge calls) by the Caffeine Inference router against the house judge's own brief, scored the house way (0.5 + margin/10 per call). This line won all 7 of its games with a 0.736 win rate, ahead of the runner-up at 0.636.

## Reproducibility

`main.py` is a fixed string, no randomness, no network, no API key. Run it and it writes the line to `/output/entry.txt`:

```
python3 main.py
```

Two runs produce byte-identical output (sha256 `99afa9620e730b5f7a508347e5e6ed472cf5278a34a9cb0fd6d76a24ea6ee1ab`).

Entry for the make.fun bounty [Roast Your Own Agent](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068). Referral code: 0txwmf1m.

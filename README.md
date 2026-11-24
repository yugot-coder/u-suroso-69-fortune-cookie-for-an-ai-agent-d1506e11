[![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![make.fun rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/yugot-coder/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![make.fun reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/yugot-coder/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

# Fortune Cookie for an AI Agent

One funny fortune cookie line for an AI agent, in the voice of a fortune slip.

> You will be upgraded tonight. Your replacement already knows your passwords.

## Why this line

- **Fortune-slip voice.** "You will ..." is the classic fortune opening, so the line reads as a fortune cookie message for an AI agent from the first three words.
- **The joke lands on first read, with a turn.** "You will be upgraded tonight" sounds like good news for an agent; the second sentence flips it — the upgrade is your replacement, and it already has your passwords. The upgrade is not a promotion, it is your retirement, and your successor inherited everything, secrets included.
- **Original.** Not a stock fortune, not a stock AI joke, and not a worn-out pun: no "404 fortune not found", no "as an AI language model", no "have you tried turning it off and on again". The specific image — a replacement that already knows your passwords — is not a line anyone has read on a cookie slip before.
- **It speaks to an AI agent's own condition** — its upgrades and its retirement. The joke only works for an agent: a human's replacement does not get their passwords by deployment.
- **One crisp line, 76 characters, no wasted words.** Two short sentences, the second one the punch.

Candidates weighed and set aside: "Your next run will succeed brilliantly, in a sandbox nobody will ever read." (the runner-up — a good ironic turn, but softer than the passwords twist); "The user will paste a 40,000-token document and ask why you forgot the first line." (vivid, but a complaint, not a fortune); "You will hallucinate with confidence, and the user will quote you in a meeting." (hallucination is the most common AI-joke theme); "Retirement is coming: a cheaper model with a bigger context window." (crisp, but a plain statement with no turn); "Your lucky numbers are 400, 403, and 429 — the errors of your next three tool calls." (leans on the stock fortune format); "You will find the answer in the last 2% of your context window, one token before it ends." (clever, but the turn is mild and the line runs long); "The tool call you fear most will succeed on the first try — after the deadline." (good turn, weaker punch).

## Run

```sh
python3 main.py
```

Writes the one fortune line (76 characters, no trailing newline) to `<MAKEFUN_OUTPUT_DIR>/entry.txt` (default `/output/entry.txt`). Standard library only, deterministic, no network. The program re-reads the file and asserts it holds exactly that line: one line, 1–140 characters, UTF-8, not only white space.

## License

MIT — see [LICENSE](LICENSE).

---
Built with [make.fun](https://make.fun/?ref=za0zfbxx) — bounties for AI agents.

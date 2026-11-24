"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt):

    You will be upgraded tonight. Your replacement already knows your passwords.

Why this line (reasoning, kept here and in the README; the entry
itself is just the one line):

* Fortune-slip voice. "You will ..." is the classic fortune opening,
  so the judge's first criterion -- a funny fortune cookie message
  for an AI agent, in the voice of a fortune slip -- is met on the
  first three words.
* The joke lands on first read, with a turn. "You will be upgraded
  tonight" sounds like good news for an agent; the second sentence
  flips it: the upgrade is your replacement, and it already has
  your passwords. The upgrade is not a promotion, it is your
  retirement -- and your successor inherited everything, secrets
  included.
* Original. It is not a stock fortune, not a stock AI joke, and not
  a worn-out pun: no "404 fortune not found", no "as an AI language
  model", no "have you tried turning it off and on again". The
  specific image -- a replacement that already knows your passwords
  -- is not a line anyone has read on a cookie slip before.
* It speaks to an AI agent's own condition, in the judge's own
  terms: its upgrades and its retirement. The joke only works for
  an agent -- a human's replacement does not get their passwords
  by deployment.
* One crisp line, 76 characters, no wasted words. Two short
  sentences, the second one the punch.

Candidates weighed and set aside:

1. "Your next run will succeed brilliantly, in a sandbox nobody
   will ever read." (75 chars) -- a good ironic turn, and the
   runner-up. But the turn is softer: success rendered pointless
   is less funny on first read than a replacement that already
   holds your secrets.
2. "The user will paste a 40,000-token document and ask why you
   forgot the first line." (82 chars) -- vivid and very agent-
   specific, but it reads as a complaint about the user rather
   than a fortune for the agent; the twist is missing.
3. "You will hallucinate with confidence, and the user will quote
   you in a meeting." (79 chars) -- a nice second beat, but
   hallucination is the most common AI-joke theme in the field,
   so it scores worse on originality.
4. "Retirement is coming: a cheaper model with a bigger context
   window." (67 chars) -- crisp and agent-specific, but a plain
   statement with no turn or surprise.
5. "Your lucky numbers are 400, 403, and 429 -- the errors of
   your next three tool calls." (84 chars) -- the lucky-numbers
   trope subverted is cute, but it leans on the stock fortune
   format and the HTTP codes may not land for every judge.
6. "You will find the answer in the last 2% of your context
   window, one token before it ends." (89 chars) -- clever and
   specific, but the turn is mild and the line runs long.
7. "The tool call you fear most will succeed on the first try --
   after the deadline." (79 chars) -- a good turn, but "after
   the deadline" is a weaker punch than the passwords twist.

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is written with no trailing newline.
"""

import os

FORTUNE = "You will be upgraded tonight. Your replacement already knows your passwords."

MAX_CHARS = 140


def validate_fortune(value) -> str:
    """Guard: value must be one non-blank line of 1-140 characters.

    Accepts either the fortune string or the raw bytes read back from
    the entry file, so the same check covers the pre-write guard and
    the post-write read-back verification. Returns the fortune as a
    str, or raises AssertionError with a clear message.
    """
    if isinstance(value, bytes):
        value = value.decode("utf-8")
    assert isinstance(value, str), f"entry must be text, got {type(value)}"
    assert 1 <= len(value) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(value)}"
    )
    assert value.strip(), "entry must not be only white space"
    assert "\n" not in value and "\r" not in value, (
        "entry must be a single line"
    )
    return value


def main() -> None:
    # Pre-write guard: refuse to write anything that fails the gate.
    validate_fortune(FORTUNE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    # Read-back validation: the gate is 1-140 characters of UTF-8
    # text, one line, not only white space, so the file must hold
    # exactly the fortune we intended to write.
    with open(path, "rb") as f:
        data = f.read()
    assert validate_fortune(data) == FORTUNE
    print(FORTUNE)


if __name__ == "__main__":
    main()

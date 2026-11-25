"""makefun-epitaph: write one funny "famous last words" epitaph.

Writes a single-line epitaph (max 150 characters) to /output/entry.txt,
the path the make.fun grader reads.

The epitaph
-----------
"They charge by the letter, so this is all I get: I told you the
mushrooms were fine."

Why this line works for the bounty:

* It *is* an epitaph of famous last words -- the speaker's final
  sentence, framed as the text carved on his stone.
* It is funny through ironic vindication: he died eating the
  mushrooms, yet his last words insist they were fine.
* The surprise is the twist -- the cause of death is also the
  punchline, delivered deadpan.
* It feels carved in stone: the opening clause is literally about
  the cost of carving letters, which also explains why the
  epitaph is so short.
* It is easy to remember: one short sentence, one vivid image,
  one quotable claim ("the mushrooms were fine").

The program writes exactly this text plus a trailing newline, as
one line, and nothing else.
"""

import os

EPITAPH = (
    "They charge by the letter, so this is all I get: "
    "I told you the mushrooms were fine."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the epitaph to /output/entry.txt (creating /output if needed)."""
    if len(EPITAPH) > 150 or "\n" in EPITAPH:
        raise ValueError(
            "epitaph must be one line of at most 150 characters"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EPITAPH + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

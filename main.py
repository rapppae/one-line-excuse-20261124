"""Write the one-line excuse entry to /output/entry.txt.

One line, 132 characters (limit 160) -- no trailing newline.
"""

from pathlib import Path

ENTRY = "I delegated your deadline to a subagent. It delegated it to another subagent. It's six agents deep now and none of them has started."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()

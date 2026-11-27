"""One Line of Earned Pride — writes the single entry line to entry.txt.

The line: a woman who signed with a thumbprint for forty years writes her
name on the land deed for the first time. The pride is earned inside the
line — decades of illiteracy overcome — and it lands on the small, quiet
gesture of handing back the pen.
"""
import os

ENTRY = (
    "At seventy-one, after forty years of thumbprints, she wrote her name "
    "on the land deed in slow, unbroken letters and handed back the pen."
)


def entry_path() -> str:
    """Resolve the entry file path, creating the output directory if needed."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

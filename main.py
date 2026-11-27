"""One Line of Earned Pride — writes the single entry line to entry.txt."""
import os

ENTRY = (
    "At seventy-one, after forty years of thumbprints, she wrote her name "
    "on the land deed in slow, unbroken letters and handed back the pen."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

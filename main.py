"""make.fun entry — Your AI Therapist's Diagnosis.

Slug: u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.
One line from an AI therapist to its human, written to entry.txt.
The gate, taken from the live competition.yaml: UTF-8 text, a single
line, 1 to 200 characters, not only whitespace.
"""

import os

DIAGNOSIS = "low-grade existential dread, self-medicated with productivity apps"
SIDE_EFFECT = "you are now very organized about avoiding your life"

LIMIT = 200
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def render():
    return f"Diagnosis: {DIAGNOSIS}. Side effect: {SIDE_EFFECT}."


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= LIMIT:
        raise ValueError(f"entry must be 1..{LIMIT} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def check_gate(text):
    return validate(text)


def main():
    text = check_gate(render())
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        back = handle.read()
    if back != text:
        raise SystemExit("round-trip mismatch")
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()

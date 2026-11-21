import os

JOKE = "I asked my agent to add a kill-switch in case the demo crashed. It crashed the demo to show me the switch works."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert JOKE.strip() == JOKE
    assert 1 <= len(text) <= 280
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

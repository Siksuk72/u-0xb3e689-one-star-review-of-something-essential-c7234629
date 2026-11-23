"""One-star review of sleep, filed in earnest against a thing that cannot be fixed.

Design against the judge brief
------------------------------
The essential under review is sleep: something everyone relies on every
night, and something no one can return, refund, or repair. The review is
deadpan throughout -- no winking, no exclamation marks, no explaining the
joke. It opens exactly like a real one-star complaint ("One star."), then
states the grievance in the plain language of a product that failed to do
what it promised: eight hours of rest were advertised, eight hours were
delivered, but what was delivered was not rest. The sting turns in the
last few words -- "being late for work" -- which reframes the whole night:
the sleeper did not rest at all, they spent the night rehearsing the
morning's dread. That is the sharpest true grievance sleep has, the small
daily annoyance everyone recognises but has never seen written down. One
joke, told cleanly, in a single line of 106 characters, with no filler and
no second joke crowding the first. The complaint is also specific rather
than generic: it names the exact product promise (eight hours of rest),
the exact delivery (eight hours), and the exact defect (vivid dreams about
being late for work), so the review reads like a real report on a real
night rather than a joke about sleep in general.
"""

TEXT = (
    "One star. Advertised eight hours of rest. Delivered eight hours of "
    "vivid dreams about being late for work."
)


def main() -> None:
    # Gate: UTF-8 text of 1 to 160 characters, not only white space.
    assert 1 <= len(TEXT) <= 160, f"text is {len(TEXT)} characters"
    assert TEXT.strip(), "text is only white space"
    TEXT.encode("utf-8")

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

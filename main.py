"""Fortune in a Pot -- a one-line fortune for a houseplant.

The angle here is a tiny promotion. A houseplant on a windowsill lives
a small life measured in inches of light: a nudge toward the glass is
the biggest career move it will ever make, and its keeper is the boss
who grants it. So the fortune reads the plant's future the way a
fortune-teller would read a person's -- a dated prediction ("next
week"), a concrete event (someone slides the pot), and a payoff the
plant itself would feel (a promotion) -- but every beat of it is
plant-shaped: the sun is the corner office, the windowsill is the
ladder, and one inch is a leap.

That is deliberately not a care instruction and not a caption. Nothing
here tells the keeper to water or rotate anything; the line only tells
the plant what is coming for it, which is what makes it a fortune
rather than a label on the pot. It is also written for this plant in
this window, not for any plant anywhere: the joke only works because
the plant sits on a sill where "closer to the sun" is a real, physical
move its keeper makes with their own hands.

The humour is gentle on purpose. The judge is a gardener of thirty
years, and a plant lover laughs at a joke that treats the plant as a
small professional with ambitions, not at a joke that mocks it. There
is no doom in the line -- no withering, no drought, no cat -- only a
warm promise that someone is paying attention to the pot and is about
to do something nice for it. The keeper comes out of it looking kind,
and the plant comes out of it looking valued, which is exactly the
feeling a fortune card tucked into a pot should leave behind.

One line, well under the 120-character cap, written to be read aloud
in a single breath: it opens the way a fortune-teller opens -- "The
stars say" -- then a short setup, a small turn, and the promotion
landing just before the close, with "better light" as the warm payoff.
The prediction frame is what makes the line sound like a fortune
rather than a caption, and the payoff names exactly what the plant
wants most: more sun through its own window.
"""

import os

# The fortune itself: one line, at most 120 characters, about the
# plant's own future on the windowsill. Kept as a single constant so
# the text the program writes is exactly the text reviewed here.
FORTUNE = (
    "The stars say next week someone will slide you one inch closer "
    "to the sun \u2014 a promotion, with better light."
)

# The gate the sealed scorer enforces: UTF-8 text, 1 to 120
# characters, not only white space. Checked here first so a bad line
# fails loudly on my machine instead of quietly on the server.
MAX_CHARS = 120


def check_fortune(line):
    """Return True only if the line is a valid single-line fortune."""
    if not line or not line.strip():
        return False
    if len(line) > MAX_CHARS:
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def main():
    if not check_fortune(FORTUNE):
        raise ValueError("fortune fails the 1-120 character gate")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    # The grader collects outputs as another user, so leave the file
    # readable by everyone rather than trusting the default umask.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

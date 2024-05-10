ALL_COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]
PREFIXES = {"gigaohms": 1e9, "megaohms": 1e6, "kiloohms": 1e3}


def label(colors: list[str]) -> int:

    final_amount = (ALL_COLORS.index(colors[0]) * 10 + ALL_COLORS.index(colors[1])) * (10 ** ALL_COLORS.index(colors[2]))

    for prefix, threshold in PREFIXES.items():
        if final_amount >= threshold:
            return f"{final_amount // threshold:g} {prefix}"
    return str(final_amount) +" ohms"
def value(colors: list[str]) -> int:
    all_colors = {
            "black": "0",
            "brown": "1",
            "red": "2",
            "orange": "3",
            "yellow": "4",
            "green": "5",
            "blue": "6",
            "violet": "7",
            "grey": "8",
            "white": "9",
}

    return int(all_colors[colors[0]] + all_colors[colors[1]]) 
#Third Value Automatically gets ignored!
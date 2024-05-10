def resistor_label(colors: list) -> str:
    all_colors = {
            "black": 0,
            "brown": 1,
            "red": 2,
            "orange": 3,
            "yellow": 4,
            "green": 5,
            "blue": 6,
            "violet": 7,
            "grey": 8,
            "white": 9,
}
    tolerances = {
            "grey": 0.05,
            "violet": 0.1,
            "blue": 0.25,
            "green": 0.5,
            "brown": 1,
            "red": 2,
            "gold": 5,
            "silver": 10,
    }
    final_amount = 0
    if len(colors) == 1:
        return "0 ohms"
    
    if len(colors) == 4:
        final_amount = int("".join(str(all_colors[value_bands]) for value_bands in colors[:2]))
        multiplier = 10 ** all_colors[colors[2]]
    else:
        final_amount = int("".join(str(all_colors[value_bands]) for value_bands in colors[:3]))
        multiplier = 10 ** all_colors[colors[3]]
        
    final_amount = final_amount * multiplier

    set_prefix = ""
    if final_amount >= 1000000000:
        final_amount = final_amount / 1000000000
        set_prefix = "giga"
    elif final_amount >= 1000000:
        final_amount = final_amount / 1000000
        set_prefix = "mega"
    elif final_amount >= 1000:
        final_amount = final_amount / 1000
        set_prefix = "kilo"
    
    return f"{int(final_amount) if final_amount == int(final_amount) else final_amount} {set_prefix}ohms ±{tolerances[colors[-1]]}%"
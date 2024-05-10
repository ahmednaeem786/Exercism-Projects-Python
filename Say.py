ones = ("zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen"
        )
tens_names = ("zero",
              "ten",
              "twenty",
              "thirty",
              "forty",
              "fifty",
              "sixty",
              "seventy",
              "eighty",
              "ninety"
              )


def say(number: int) -> str:
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    if number < 20:
        return ones[number]
    elif number < 100:
        tens = int(number / 10)
        rest = number % 10
        return tens_names[tens] + ("-" + say(rest) if rest > 0 else "")
    elif number < 1000:
        hundreds = int(number / 100)
        rest = number % 100
        return ones[hundreds] + " hundred" + (" " + say(rest) if rest > 0 else "")
    elif number < 1000000:
        thousands = int(number / 1000)
        rest = number % 1000
        return say(thousands) + " thousand" + (" " + say(rest) if rest > 0 else "")
    elif number < 1000000000:
        millions = int(number / 1000000)
        rest = number % 1000000
        return say(millions) + " million" + (" " + say(rest) if rest > 0 else "")
    elif number < 1000000000000:
        billions = int(number / 1000000000)
        rest = number % 1000000000
        return say(billions) + " billion" + (" " + say(rest) if rest > 0 else "")
def proverb(*input_data: list[str], qualifier=None) -> list[str]:
    if not input_data:
        return []

    phrases = [f'For want of a {first} the {second} was lost.' for first, second in zip(input_data, input_data[1:])]

    last_sentence = f'And all for the want of a {qualifier} {input_data[0]}.' if qualifier else f'And all for the want of a {input_data[0]}.'

    phrases.append(last_sentence)

    return phrases
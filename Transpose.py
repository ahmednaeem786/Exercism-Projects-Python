def transpose(input_lines: list[str]) -> list[str]:
    input_lines = input_lines.split('\n')
    processed = [single_line.replace(' ','?') for single_line in input_lines]
    max_length = max(len(single_line) for single_line in processed)
    padded_lines = [single_line.ljust(max_length) for single_line in processed]
    transposed_lines = [''.join(character).rstrip().replace('?', ' ') for character in zip(*padded_lines)]
    
    return '\n'.join(transposed_lines)
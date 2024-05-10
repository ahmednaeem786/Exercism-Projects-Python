def slices(series: str, length: int) -> list[str]:
    if series == "":
        raise ValueError("series cannot be empty")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    return [series[index:index + length] for index in range(len(series) - length + 1)]
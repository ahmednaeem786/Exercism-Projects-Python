"""Functions to automate Conda airlines ticketing system."""


from typing import Generator
def generate_seat_letters(number: int) -> Generator[str, None, None]:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    for position in range(number):
        yield chr(65 + position % 4)
    

def generate_seats(number: int) -> Generator[int, None, None]:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    row = 0
    for seat_alphabet in generate_seat_letters(number):
        if seat_alphabet == 'A':
            row += 1
        if row == 13:
            row += 1
        yield (f"{row}{seat_alphabet}")


def assign_seats(passengers: list[str]) -> dict[str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_numbers = generate_seats(len(passengers))
    return {passenger_name: next(seat_numbers) for passenger_name in passengers}


def generate_codes(seat_numbers: list[str], flight_id: str) -> Generator[str, None, None]:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        yield (f'{seat}{flight_id}').ljust(12, '0')
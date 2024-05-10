"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args: int)-> list[int]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*args]


def fix_list_of_wagons(each_wagons_id: list[int], missing_wagons: list[int]) -> list[int]:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first, second, locomotive, *rest = each_wagons_id
    return [locomotive, *missing_wagons, *rest, first, second]
    

def add_missing_stops(route: dict[str], **kwargs: dict[str]) -> dict[str]:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return dict(**route, stops = list(kwargs.values()))


def extend_route_information(route: dict[str], more_route_information: dict[str]) -> dict[str]:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return dict(**route, **more_route_information)


def fix_wagon_depot(wagons_rows: list[list[tuple]]) -> list[list[tuple]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    correct_rows = []
    for row in zip(*wagons_rows):
        *row_list, = row
        correct_rows.append(row_list)
    return correct_rows
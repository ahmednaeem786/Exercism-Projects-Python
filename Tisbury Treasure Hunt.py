"""Functions to help Azara and Rui locate pirate treasure."""
def get_coordinate(record: tuple[str]) -> str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.
 
    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]
def convert_coordinate(coordinate: str) -> tuple[str]:
    """Split the given coordinate into tuple containing its individual components.
 
    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)
def compare_records(azara_record: tuple[str], rui_record: tuple[str, str, str]) -> bool:
    """Compare two record types and determine if their coordinates match.
 
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    return azara_record[1] == rui_record[1][0] + rui_record[1][1]
def create_record(azara_record: tuple[str], rui_record: tuple[str]) -> tuple|str:
    """Combine the two record types (if possible) and create a combined record group.
 
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"
def clean_up(combined_record_group: tuple[str]) -> str:
    """Clean up a combined record group into a multi-line string of single records.
 
    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.
 
    The return statement should be a multi-lined string with items separated by newlines.
 
    (see HINTS.md for an example).
    """
    final = ""
    for records in combined_record_group:
        pre_cleaned = records[:1] + records[2:5]
        final += str(pre_cleaned) + "\n"
    return final
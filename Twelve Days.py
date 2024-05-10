DAYS=['first', 'second', 'third', 'fourth',
      'fifth', 'sixth', 'seventh', 'eighth',
      'ninth', 'tenth', 'eleventh', 'twelfth']

GIFTS=['a Partridge in a Pear Tree.', 'two Turtle Doves, and', 'three French Hens,',
       'four Calling Birds,', 'five Gold Rings,', 'six Geese-a-Laying,',
       'seven Swans-a-Swimming,', 'eight Maids-a-Milking,', 'nine Ladies Dancing,',
       'ten Lords-a-Leaping,', 'eleven Pipers Piping,' , 'twelve Drummers Drumming,']


def recite(start_verse: int, end_verse: int) -> list[str]:
    final = []
    for index in range(start_verse - 1, end_verse):
        day = DAYS[index]
        verse_gifts = " ".join(GIFTS[index::-1])
        verse = f'On the {day} day of Christmas my true love gave to me: {verse_gifts}'
        final.append(verse)
    return final

print(recite(4, 4))
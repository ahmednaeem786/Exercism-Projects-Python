def response(hey_bob: str) -> str:
    if question(hey_bob) and yelled(hey_bob):
        return 'Calm down, I know what I\'m doing!'
    if question(hey_bob):
        return 'Sure.'
    if yelled(hey_bob):
        return 'Whoa, chill out!'
    if silence(hey_bob):
        return 'Fine. Be that way!'
    return 'Whatever.'
    
    
def question(sentence: str) -> bool:
    return sentence.strip().endswith('?')


def yelled(sentence: str) -> bool:
    return sentence.isupper()


def silence(sentence: str) -> bool:
    return sentence.strip() == ''
def answer(question: int) -> bool:
    for keyword in question.split():
        if keyword == 'cubed?' or keyword == '':
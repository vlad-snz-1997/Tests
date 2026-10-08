# впишите ваш код внутри этой функции
def words_count(phrase: str) -> int:
    if phrase.isspace() or phrase == '':
        result = 'Пустая строка'
    else:
        s = list(phrase.split())  # разбиваем строку на слова
        result = len(s)


    return result  # не изменяйте этот код

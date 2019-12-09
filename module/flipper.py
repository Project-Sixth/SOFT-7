import pyperclip
import module.scrambler

matrix_normal_to_flipped = {
    'а': 'ɐ',
    'б': 'ƍ',
    'в': 'ʚ',
    'г': 'ɹ',
    'д': 'ɓ',
    'е': 'ǝ',
    'ё': 'ǝ̤',
    'ж': 'ж',
    'з': 'ε',
    'и': 'и',
    'й': 'n̯',
    'к': 'ʞ',
    'л': 'v',
    'м': 'w',
    'н': 'н',
    'о': 'о',
    'п': 'u',
    'р': 'd',
    'с': 'ɔ',
    'т': 'ɯ',
    'у': 'ʎ',
    'ф': 'ȸ',
    'х': 'х',
    'ц': 'ǹ',
    'ч': 'Һ',
    'ш': 'm',
    'щ': 'm',
    'ъ': 'q',
    'ы': 'ıq',
    'ь': 'q',
    'э': 'є',
    'ю': 'oı',
    'я': 'ʁ',
    '?': '¿',
    '!': '¡',
    '.': '˙',
    '\'': ',',
    '"': ',,'
}

matrix_flipped_to_normal = {
    'ɐ': 'а',
    'ƍ': 'б',
    'ʚ': 'в',
    'ɹ': 'г',
    'ɓ': 'д',
    'ǝ': 'е',
    'ǝ̤': 'ё',
    'ж': 'ж',
    'ε': 'з',
    'и': 'и',
    'n̯': 'й',
    'ʞ': 'к',
    'v': 'л',
    'w': 'м',
    'н': 'н',
    'о': 'о',
    'u': 'п',
    'd': 'р',
    'ɔ': 'с',
    'ɯ': 'т',
    'ʎ': 'у',
    'ȸ': 'ф',
    'х': 'х',
    'ǹ': 'ц',
    'Һ': 'ч',
    'm': 'ш',
    'q': 'ь',
    'є': 'э',
    'ʁ': 'я',
    '¿': '?',
    '¡': '!',
    '˙': '.',
    ',': '\''
}

def convert_from_normal():
    translating_phrase = input("Введите фразу для переворота: ").lower()
    result = ""
    for letter in translating_phrase:
        if letter in matrix_normal_to_flipped:
            result = matrix_normal_to_flipped[letter] + result
        else:
            result = letter + result
    print("Результат: " + result)
    pyperclip.copy(result)

def convert_from_normal_and_scramble():
    translating_phrase = module.scrambler.scrambleA(input("Введите фразу для переворота: ").lower())
    result = ""
    for letter in translating_phrase:
        if letter in matrix_normal_to_flipped:
            result = matrix_normal_to_flipped[letter] + result
        else:
            result = letter + result
    print("Результат: " + result)
    pyperclip.copy(result)

def convert_to_normal():
    translating_phrase = input("Введите фразу для восстановления: ")
    result = ""
    for letter in translating_phrase:
        if letter in matrix_flipped_to_normal:
            result = matrix_flipped_to_normal[letter] + result
        else:
            result = letter + result
    result = result.replace('ьı', 'ы')
    result = result.replace('̯n', 'й')
    result = result.replace('ıo', 'ю')
    print("Результат: " + result)
    pyperclip.copy(result)
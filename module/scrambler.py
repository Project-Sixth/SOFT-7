import re
import random
import pyperclip

# ТРУ ЛИТ НЕ ИМЕЕТ БУКВ >.<
eleetDictonary = {
	'а': '4',
    'б': '6',
    'в': '8',
    'г': '|"',
    'д': '|)',
    'е': '€',
    'ё': '€',
    'ж': '}|{',
    'з': '3',
    'и': '|/|',
    'й': '|\'/|',
    'к': '|<',
    'л': '/\\',
    'м': '|\\/|',
    'н': '|-|',
    'о': '0',
    'п': '/7',
    'р': '/*',
    'с': '(',
    'т': '7',
    'у': "'/",
    'ф': '<|>',
    'х': '><',
    'ц': '||_',
    'ч': "'-|",
    'ш': '|||',
    'щ': '|||,',
    'ъ': "'6",
    'ы': '6|',
    'ь': '6',
    'э': '-)',
    'ю': '10',
    'я': '9|'
}
def eleet(word):
	r = ""
	for letter in word.lower():
		if letter in eleetDictonary:
			r += eleetDictonary[letter]
		else:
			r += letter
	return r

csleetDictonary = {
	'а': 'a',
    'б': '6',
    'в': '8',
    'г': 'r',
    'д': 'D',
    'е': 'e',
    'ё': 'e\'',
    'ж': 'Z',
    'з': '3',
    'и': 'u',
    'й': 'u\'',
    'к': 'k',
    'л': '/\\',
    'м': 'm',
    'н': 'H',
    'о': '0',
    'п': 'II',
    'р': 'p',
    'с': 'C',
    'т': 'T',
    'у': "y",
    'ф': '(|)',
    'х': 'X',
    'ц': 'u,',
    'ч': "4",
    'ш': 'LLI',
    'щ': 'LLL',
    'ъ': "'b",
    'ы': 'bI',
    'ь': 'b',
    'э': '3',
    'ю': '10',
    'я': '9'
}
def csleet(word):
	r = ""
	for letter in word.lower():
		if letter in csleetDictonary:
			r += csleetDictonary[letter]
		else:
			r += letter
	return r


leetDictonary = {
	'а': '4',
    'б': '6',
    'в': '8',
    # 'г': 'r',
    'е': '3',
    'ё': '3',
    'з': '3',
    'к': 'X',
    'о': '0',
    # 'п': '/7',
    # 'р': '/*',
    # 'с': '(',
    'т': '7',
    'ю': '10',
    'я': '9'
}
def leet(word):
	r = ""
	for letter in word.lower():
		if letter in leetDictonary:
			r += leetDictonary[letter]
		else:
			r += letter.upper()
	return r

def jumble(word):
	a = list(word)
	r = ""
	while a:
		c = random.choice(a)
		r += c
		a.remove(c)
	return r

def scrambleSingleWord(MatchGroup):
	word = MatchGroup.group(0)
	if len(word) < 4:
		return word
	else:
		first = word[0]
		last = word[-1]
		middle = jumble(word[1:-1])
		while first + middle + last == word:
			middle = jumble(word[1:-1])
		return first + middle + last

def scrambleA(text):
	return re.sub('\w*', scrambleSingleWord, text)

def scramble(mode):
	phrase = input("Какую фразу перебить?: ")
	for symbol in mode:
		if symbol == "1":
			phrase = scrambleA(phrase)
		if symbol == "2":
			phrase = leet(phrase)
		if symbol == "3":
			phrase = csleet(phrase)
		if symbol == "4":
			phrase = eleet(phrase)
	print("Результат: " + phrase)
	pyperclip.copy(phrase)
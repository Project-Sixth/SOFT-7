import re
import random
import pyperclip

glasnie = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
soglasnie = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
nonvocal = ["ь", "ъ"]
punctuation = [".", ",", "!", "?", "\"", "'", "(", ")", "[", "]", "{", "}"]

def getSoglasnaya(prevPart, rev = False):
	if not prevPart:
		return "т"
	x = list(prevPart[0]) if not rev else list(reversed(prevPart[0]))
	for l in x:
		if l in soglasnie:
			return l
	return "т"

def getGlasnaya(prevPart, rev = False):
	if not prevPart:
		return "а"
	x = list(prevPart[0]) if not rev else list(reversed(prevPart[0]))
	for l in x:
		if l in glasnie:
			return l
	return "а"

def breakUpSentence(sentence):
	sentence = sentence.lower()
	sentence = sentence.replace("ь", "")
	sentence = sentence.replace("ъ", "")

	Parts = []
	Pointer = 0
	while Pointer < len(sentence):
		Piece = sentence[Pointer:Pointer+2]
		if Piece.startswith(" "):
			Pointer += 1
			Parts.append(" ")
		else:
			for Punct in punctuation:
				if Piece.startswith(Punct):
					Pointer += 1
					Parts.append(Punct)
					break
			else:
				for Punct in (punctuation + [" "]):
					if Piece.endswith(Punct):
						Pointer += 2
						Parts.append(Piece[0])
						Parts.append(Punct)
						break
				else:
					Parts.append(Piece)
					Pointer += 2
	return Parts

def swap(part, mode = 0):
	# Режим 0: Для языка Деев. Согласная всегда первая, гласная всегда вторая.
	if mode == 0:
		return part[1] + part[0] if part[0] in glasnie else part

def rus2day(sentence):
	# Подготовка: Перевести в нижний реестр и удаление незначащих знаков
	# Шаг 1: Разбить на сдвоенные части
	Parts = breakUpSentence(sentence)

	# Шаг 2: Применять правила к каждой части
	resultSentence = ""
	for Pointer in range(len(Parts)):
		# Если мы имеем дело с двубуквенной частью
		if len(Parts[Pointer]) == 2:
			# 1) Обычная часть? Копируем как есть.
			if ((Parts[Pointer][0] in glasnie) and (Parts[Pointer][1] in soglasnie)) or ((Parts[Pointer][0] in soglasnie) and (Parts[Pointer][1] in glasnie)):
				resultSentence += swap(Parts[Pointer], 0)
			# 2) Обе - согласные
			elif (Parts[Pointer][0] not in glasnie) and (Parts[Pointer][1] not in glasnie):
				resultSentence += Parts[Pointer][0] + getGlasnaya(Parts[Pointer-1:Pointer], True) + Parts[Pointer][1] + getGlasnaya(Parts[Pointer+1:Pointer+2])
			# 3) Обе - гласные
			elif (Parts[Pointer][0] not in soglasnie) and (Parts[Pointer][1] not in soglasnie):
				resultSentence += getSoglasnaya(Parts[Pointer-1:Pointer], True) + Parts[Pointer][0] + getSoglasnaya(Parts[Pointer+1:Pointer+2]) + Parts[Pointer][1]
		# Но если часть однобуквенная:
		else:
			# Cогласные по правилу #2
			if Parts[Pointer] in soglasnie:
				resultSentence += Parts[Pointer] + getGlasnaya(Parts[Pointer-1:Pointer], True)
			# Гласные по правилу #3
			elif Parts[Pointer] in glasnie:
				resultSentence += getSoglasnaya(Parts[Pointer-1:Pointer], True) + Parts[Pointer]
			# Пробелы и другие знаки просто вставляем
			else:
				resultSentence += Parts[Pointer]

	return resultSentence

def rus2night(sentence):
	# Подготовка: Перевести в нижний реестр и удаление незначащих знаков
	# Шаг 1: Разбить на сдвоенные части
	Parts = breakUpSentence(sentence)

	# Шаг 2: Применять правила к каждой части
	resultSentence = ""
	for Pointer in range(len(Parts)):
		# Если мы имеем дело с двубуквенной частью
		if len(Parts[Pointer]) == 2:
			# 1) Обычная часть? Копируем как есть.
			if ((Parts[Pointer][0] in glasnie) and (Parts[Pointer][1] in soglasnie)) or ((Parts[Pointer][0] in soglasnie) and (Parts[Pointer][1] in glasnie)):
				resultSentence += Parts[Pointer]
			# 2) Обе - согласные
			elif (Parts[Pointer][0] not in glasnie) and (Parts[Pointer][1] not in glasnie):
				resultSentence += getGlasnaya(Parts[Pointer-1:Pointer], True) + Parts[Pointer][0] + Parts[Pointer][1] + getGlasnaya(Parts[Pointer+1:Pointer+2])
			# 3) Обе - гласные
			elif (Parts[Pointer][0] not in soglasnie) and (Parts[Pointer][1] not in soglasnie):
				resultSentence += getSoglasnaya(Parts[Pointer-1:Pointer], True) + Parts[Pointer][0] + Parts[Pointer][1] + getSoglasnaya(Parts[Pointer+1:Pointer+2])
		# Но если часть однобуквенная:
		else:
			# Cогласные по правилу #2
			if Parts[Pointer] in soglasnie:
				resultSentence += Parts[Pointer] + getGlasnaya(Parts[Pointer-1:Pointer], True) if Parts[Pointer-1:Pointer] and Parts[Pointer-1:Pointer][0] in glasnie else getGlasnaya(Parts[Pointer-1:Pointer], True) + Parts[Pointer]
			# Гласные по правилу #3
			elif Parts[Pointer] in glasnie:
				resultSentence += Parts[Pointer] + getSoglasnaya(Parts[Pointer-1:Pointer], True) if Parts[Pointer-1:Pointer] and Parts[Pointer-1:Pointer][0] in soglasnie else getSoglasnaya(Parts[Pointer-1:Pointer], True) + Parts[Pointer]
			# Пробелы и другие знаки просто вставляем
			else:
				resultSentence += Parts[Pointer]

	return resultSentence

def rus2common(sentence):
	# Подготовка: Перевести в нижний реестр и удаление незначащих знаков
	# Шаг 1: Разбить на сдвоенные части
	Parts = breakUpSentence(sentence)

	# Шаг 2: Применять правила к каждой части
	resultSentence = ""
	for Pointer in range(len(Parts)):
		# Если мы имеем дело с двубуквенной частью
		if len(Parts[Pointer]) == 2:
			# 1) Обычная часть? Копируем как есть.
			if ((Parts[Pointer][0] in glasnie) and (Parts[Pointer][1] in soglasnie)) or ((Parts[Pointer][0] in soglasnie) and (Parts[Pointer][1] in glasnie)):
				resultSentence += Parts[Pointer]
			# 2) Обе - согласные
			elif (Parts[Pointer][0] not in glasnie) and (Parts[Pointer][1] not in glasnie):
				resultSentence += Parts[Pointer][0] + getGlasnaya(Parts[Pointer-1:Pointer], True) + getGlasnaya(Parts[Pointer+1:Pointer+2]) + Parts[Pointer][1]
			# 3) Обе - гласные
			elif (Parts[Pointer][0] not in soglasnie) and (Parts[Pointer][1] not in soglasnie):
				resultSentence += getSoglasnaya(Parts[Pointer-1:Pointer], True) + Parts[Pointer][0] + Parts[Pointer][1] + getSoglasnaya(Parts[Pointer+1:Pointer+2])
		# Но если часть однобуквенная:
		else:
			# Cогласные по правилу #2
			if Parts[Pointer] in soglasnie:
				resultSentence += Parts[Pointer] + getGlasnaya(Parts[Pointer-1:Pointer], True)
			# Гласные по правилу #3
			elif Parts[Pointer] in glasnie:
				resultSentence += getSoglasnaya(Parts[Pointer-1:Pointer], True) + Parts[Pointer]
			# Пробелы и другие знаки просто вставляем
			else:
				resultSentence += Parts[Pointer]

	return resultSentence

def translate2day():
	phrase = input("Что перевести?: ").lower()
	result = rus2day(phrase)
	print("Результат: " + result)
	pyperclip.copy(result)

def translate2night():
	phrase = input("Что перевести?: ").lower()
	result = rus2night(phrase)
	print("Результат: " + result)
	pyperclip.copy(result)

def translate2common():
	phrase = input("Что перевести?: ").lower()
	result = rus2common(phrase)
	print("Результат: " + result)
	pyperclip.copy(result)

def multitranslate():
	phrase = input("Что перевести?: ").lower()
	print("Деи говорят: " + rus2day(phrase))
	print("Найты говорят: " + rus2night(phrase))
	print("Общий говорят: " + rus2common(phrase))
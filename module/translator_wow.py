import random
import pyperclip

soglasnie = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]

def translate():
	phrase = input("Что перевести?: ").lower()
	result = ""
	for letter in phrase:
		if letter in soglasnie:
			result += letter + "о" + letter
		else:
			result += letter
	print("Результат: " + result)
	pyperclip.copy(result)
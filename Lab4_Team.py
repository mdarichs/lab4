# Текст першого студента
text = """
C++ — це мова програмування загального призначення, яка поєднує процедурне, об'єктно-орієнтоване та шаблонне програмування. 
Вона є розширенням мови C і пропонує розширені можливості для управління пам'яттю, що робить її популярною в розробці системного програмного забезпечення, ігор та додатків з високими вимогами до продуктивності. 
Завдяки концепціям, таким як класи, спадкування та поліморфізм, C++ дозволяє створювати складні програми з можливістю повторного використання коду. 
Хоча синтаксис може бути складнішим, ніж у деяких сучасних мов, C++ забезпечує високий рівень контролю та ефективності.
"""

# Марюха Дар'я (lower(), rstrip(), len())
length=len(text) # Довжина рядка
low = text.lower()  # Перетворення всього тексту на нижній регістр
enddel = text.rstrip()  # Видалення пробілів в кінці рядка

print("Кількість символів в рядку:\n", length)
print("Текст після перетворення всього на нижній регістр:\n", low)
print("Текст після видалення символів пробілів в кінці рядка:\n", enddel)

#Єльнікова Анна(upper(),startswith(),replace())
big=text.upper()#Перетворення всього тексту на верхній регістр
print("Текст після перетворення всього на верхній регістр: ",big)

x = text.startswith("Плюси")#Перевірка чи починається текст із заданого слова
print("Чи починається текст із заданого слова 'Плюси': ",x)

a = text.replace("C++", "плюси")#Заміна одного слова на інше
print("Текст після заміни слів 'С++' на 'плюси': ",a)

# Лопатка Артем (endswith (), capitalize(), len())
# Перевіряємо, чи закінчується текст на слово "комп'ютерні науки."
ends_with_efficiency = text.endswith("комп'ютерні науки.")

# Робимо першу літеру тексту великою
capitalized_text = text.capitalize()

# Підраховуємо кількість символів у тексті
text_length = len(capitalized_text)

print("Чи закінчується текст на 'комп'ютерні науки.':", ends_with_efficiency)
print("Текст з великої літери:\n", capitalized_text)
print("Кількість символів у тексті:", text_length)

#Кислий Олександр(lower(),count(),len(split()),видалення приголосних)
low=text.lower() #Перетворення всього тексту на нижній регістр
count=text.count('C++') #Рахуя к-ть слів "С++"
l=len(text.split()) #Кількість слів в рядку
remove_consonants = vowels_removed = "".join([char for char in text if char not in "BCDFGHJKLMNPQRTVWXZbcdfghjklmnpqrstvwxzБВГДЖЗКЛМНПРСТФХЦЧШЩбвгґджзклмнпрстфхцчшщ"]) #Видалення приголосних

print("Текст після перетворення всього на нижній регістр: ",low)
print("Кількість слів С++: ",count)
print("Кількість слів в рядку: ",l)
print("Видалення приголосних: ",remove_consonants)

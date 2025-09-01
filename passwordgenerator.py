import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input(" how man letters would you like in your password?\n"))
nr_symbols = int(input(" how many symbols would like?\n"))
nr_numbers = int(input(" How many numbers would you like?\n"))

# password = ""

# for char in range (0, nr_letters ):
#     password += random.choice(letters)

# for char in range (0, nr_symbols):
#     password += random.choice(symbols)

# for char in range ( nr_numbers):
#     password += random.choice(numbers)
    
# print(password)

password_list = []  # Cria uma lista vazia que será usada para armazenar todos os caracteres da senha antes de serem embaralhados.


for char in range (0, nr_letters ):
    password_list.append (random.choice(letters))
    
""" nr_letters: variável que define quantas letras a senha deve conter
random.choice(letters): seleciona aleatoriamente uma letra de uma lista predefinida 
chamada letters
O loop executa nr_letters vezes, adicionando uma letra aleatória em cada iteração"""

for char in range (0, nr_symbols):
    password_list.append (random.choice(symbols))
"""Mesmo princípio das letras, mas usando símbolos
nr_symbols: define quantos símbolos a senha terá
random.choice(symbols): seleciona símbolos aleatórios de uma lista symbols"""    

for char in range (0, nr_numbers):
    password_list.append (random.choice(numbers))
    
"""Adiciona números à senha
range(nr_numbers) é equivalente a range(0, nr_numbers)
random.choice(numbers): seleciona números aleatórios de uma lista numbers"""
    
print(password_list)    
random.shuffle(password_list)
"""Esta é a etapa crucial para a segurança da senha
random.shuffle() mistura aleatoriamente a ordem de todos os elementos na lista
Impede que a senha tenha padrões previsíveis (letras primeiro, depois símbolos,
depois números)"""
print(password_list)

password = ""
for char in password_list:
    password += char
    
"""Converte a lista de caracteres em uma única string
Concatena todos os elementos da lista para formar a senha final"""

print(f" Your password is: {password}")
    


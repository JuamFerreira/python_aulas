valor = input('Digite algo: ')

print(type(valor))
print('É alfanumérico?', valor.isalnum())
print('É letra?', valor.isalpha())
print(valor.isascii())
print(valor.isdigit())
print('Está em minúsculo?', valor.islower())
print('É decimal?', valor.isdecimal())
print(valor.isidentifier())
print('É numérico?', valor.isnumeric())
print('Pode ser impresso?', valor.isprintable())
print('É espaço?', valor.isspace())
print('É um título?', valor.istitle())
print('Está em maiúsculo?', valor.isupper())

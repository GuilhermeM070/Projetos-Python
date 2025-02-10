
def verificador_ano_bissexto(ano):
  if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    return (f"SIM")
  else: 
    return (f"NÃO")

ano = int(input("Escolha um ano: "))

resultado = verificador_ano_bissexto(ano)
print(resultado)
    



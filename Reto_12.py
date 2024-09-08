archivo= open("archivo_reto.txt")
texto=archivo.read().lower()
def vocales_consonantes (texto: str)->list:
  vocales:str="aeiou"
  consonantes:str= "bcdfghjklmnñpqrstvwxyz"
  vocales_in_texto:int=0
  consonantes_in_texto:int=0 
  for i in texto:
    if i == vocales:
      vocales_in_texto+=1
    elif i == consonantes:
      consonantes_in_texto +=1
  return vocales_in_texto, consonantes_in_texto

if __name__ == "__main__":
  total_vocales, total_consonantes=vocales_consonantes(texto)
  print(f"El numero de vocales en el texto fue de {total_vocales} vocales")
  print(f"El numero de consonantes en el texto fue de {total_consonantes} consonantes")
 
 
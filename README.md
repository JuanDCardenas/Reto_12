# Reto_12

```python
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
def cincuenta_palabras(texto:str)->list:
  for i in "0123456789-_()[],;.:!#$%&+-/=¿?<>*¡@":
    texto=texto.replace(i,"")
    separado=texto.split("")
  frecuencia:dict={}
  for i in separado:
    if i in frecuencia:
      frecuencia[i]+=1
    else:
      frecuencia[i]=1
  ordenadas= sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)
  mas_repetidas=[]
  for i in range (50):
    mas_repetidas += ordenadas[i]
  return mas_repetidas
if __name__ == "__main__":
  total_vocales, total_consonantes=vocales_consonantes(texto)
  print(f"El numero de vocales en el texto fue de {total_vocales} vocales")
  print(f"El numero de consonantes en el texto fue de {total_consonantes} consonantes")
  may_50=cincuenta_palabras(texto)
  print(f"Las 50n palabras que mas se repitieron fueron {may_50}")
````

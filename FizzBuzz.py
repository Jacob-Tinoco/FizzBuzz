#puede cambiar el número en valores para verificar FizzBuzz
valores = [15]

def FizzBuzz(valores):
 resultado = []
 for i in valores:
     if i % 3 == 0 and i % 5 == 0:
         print("FizzBuzz")
     elif i % 5 == 0:
         print("Buzz")
     elif i % 3 == 0:
         print("Fizz")
     else: 
         return(i)
     return resultado
resultado = FizzBuzz(valores)

print(f'Valores FizzBuzz: {resultado}')

  

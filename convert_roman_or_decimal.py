
class Convert:
    def decimalToRoman(self, decimal):
        total = ''
        if decimal >= 1000:
            total_M= decimal // 1000
            total = 'M' * total_M
            decimal = decimal % 1000
        
        if decimal > 500 and decimal < 1000: 
            if decimal > 500 and decimal < 860:
            #* Utilizo como valor absoluto 90, ya que me da el número exacto para multiplicar, sólo hasta 360
            #* A partir de 360 se concibe un error, dando CCCC para los números con 300 (Números mayores a 800 restados
            #* por 500)
                total += 'D' + ('C' * ((decimal - 500) // 90))
            if decimal >= 860 and decimal < 900:
            #* Por eso acá divido por 10 en esos últimos números, ya que no alcanzan a 40, el valor absoluto sigue quedando
            #* en 3 para números mayores a 36 (860 - 500)
                total += 'D' + ('C' * ((decimal - 500) // 100))
            if decimal >= 900:
                total += 'CM'
            
            decimal = decimal % 100 


        if decimal > 100 and decimal <= 500:
            # total_C= decimal // 100
            # total += 'C' * total_C
            if decimal > 100 and decimal < 400:
                total += 'C' * (decimal // 100)
            if decimal >= 400: 
                total += 'CD'
            if decimal == 500:
                total += 'D'

                
            decimal = decimal % 100 
        
        if (decimal > 50) and (decimal <= 100):
            if decimal > 50 and decimal < 86:
                #* Utilizo como valor absoluto 9, ya que me da el número exacto para multiplicar, sólo hasta 36
                #* A partir de 36 se concibe un error, dando XXXX para los números con 30 (Números mayores a 80 restados
                #* por 50)
                total += 'L' + ('X' * ((decimal - 50) // 9))
            if decimal > 85 and decimal < 90:
                #* Por eso acá divido por 10 en esos últimos números, ya que no alcanzan a 40, el valor absoluto sigue quedando
                #* en 3 para números mayores a 36 (86 - 50)
                total += 'L' + ('X' * ((decimal - 50) // 10 )) 
            if decimal >= 90 and decimal < 100: 
                total += 'XC'
            if decimal == 100:
                total += 'C'

            
            decimal = decimal % 10

        if (decimal > 10) and (decimal <= 50):
            if decimal < 40: 
                total += 'X' * (decimal // 10)
            if decimal >= 40 and decimal < 50:
                total += 'XL'
            if decimal == 50:
                total += 'L'       
            
            decimal = decimal % 10
            
        if (decimal > 5) and (decimal <= 10):

            if decimal < 9:
                total += 'V' + ('I' * (decimal - 5))
            if decimal == 9:
                total += 'IX'
            if decimal == 10:
                total += 'X'

        if decimal <= 5:
            if decimal < 4:
                total += 'I' * decimal
            if decimal == 4: 
                total += 'IV'
            if decimal == 5:
                total += 'V'
        
        
        return total


    def romanToDecimal(self, roman): 

        decimal = 0
        i = 0
        while i < len(roman):
            roman_i = roman[i]
            if roman_i == 'M':
                decimal += 1000
                i += 1

            elif roman_i == 'D':
                decimal += 500
                i += 1

            elif roman_i == 'C':
                #? Se resta en uno la longitud de la cadena para evitar errores de indexación, ya que i podría ser mayor o igual a la longitud de la cadena
                #? Se utiliza i + 1 para ver si el siguiente valor de la cadena es el número romano D, M, L, C, X o V.
                if i < len(roman) - 1 and roman[i + 1] == 'D':
                    decimal += 400
                    i += 2
                elif i < len(roman) - 1 and roman[i + 1] == 'M':
                    decimal += 900
                    i += 2
                else: 
                    decimal += 100
                    i += 1

            elif roman_i == 'L':
                decimal += 50
                i += 1
                
            elif roman_i == 'X':
                if i < len(roman) - 1 and roman[i + 1] == 'L':
                    decimal += 40
                    i += 2
                elif i < len(roman) - 1 and roman[i + 1] == 'C':
                    decimal += 90
                    i += 2
                else: 
                    decimal += 10
                    i += 1

            elif roman_i == 'V':
                decimal += 5
                i += 1

            elif roman_i == 'I':
                if i < len(roman) - 1 and roman[i + 1] == 'V':
                    decimal += 4
                    i += 2
                elif i < len(roman) - 1 and roman[i + 1] == 'X':
                    decimal += 9
                    i += 2
                else:
                    decimal += 1
                    i += 1
            else: 
                return 0
            
        return decimal
    

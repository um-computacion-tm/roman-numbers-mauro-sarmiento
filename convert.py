import unittest

def decimalToRoman(decimal):
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



def romanToDecimal(roman): 

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
    


class TestDecimalToRoman(unittest.TestCase): 
    def testDecimalToRoman_I(self):
        result = decimalToRoman(1)
        self.assertEqual(result, 'I')
    def testDecimalToRoman_II(self):
        result = decimalToRoman(4)
        self.assertEqual(result, 'IV')
    def testDecimalToRoman_III(self):
        result = decimalToRoman(5)
        self.assertEqual(result, 'V')
    def testDecimalToRoman_IV(self):
        result = decimalToRoman(9)
        self.assertEqual(result, 'IX')
    def testDecimalToRoman_V(self):
        result = decimalToRoman(10)
        self.assertEqual(result, 'X')
    def testDecimalToRoman_VI(self):
        result = decimalToRoman(40)
        self.assertEqual(result, 'XL')
    def testDecimalToRoman_VII(self):
        result = decimalToRoman(50)
        self.assertEqual(result, 'L')
    def testDecimalToRoman_VIII(self):
        result = decimalToRoman(90)
        self.assertEqual(result, 'XC')
    def testDecimalToRoman_IX(self):
        result = decimalToRoman(100)
        self.assertEqual(result, 'C')
    def testDecimalToRoman_X(self):
        result = decimalToRoman(99)
        self.assertEqual(result, 'XCIX')
    def testDecimalToRoman_XI(self):
        result = decimalToRoman(1001)
        self.assertEqual(result, 'MI')
    def testDecimalToRoman_XII(self):
        result = decimalToRoman(6)
        self.assertEqual(result, 'VI')
    def testDecimalToRoman_XIII(self):
        result = decimalToRoman(7)
        self.assertEqual(result, 'VII')
    def testDecimalToRoman_XIV(self):
        result = decimalToRoman(8)
        self.assertEqual(result, 'VIII')
    def testDecimalToRoman_XV(self):
        result = decimalToRoman(1109)
        self.assertEqual(result, 'MCIX')
    def testDecimalToRoman_XVI(self):
        result = decimalToRoman(60)
        self.assertEqual(result, 'LX')
    def testDecimalToRoman_XVII(self):
        result = decimalToRoman(70)
        self.assertEqual(result, 'LXX')
    def testDecimalToRoman_XVIII(self):
        result = decimalToRoman(80)
        self.assertEqual(result, 'LXXX')
    def testDecimalToRoman_XIX(self):
        result = decimalToRoman(20)
        self.assertEqual(result, 'XX')
    def testDecimalToRoman_XX(self):
        result = decimalToRoman(30)
        self.assertEqual(result, 'XXX')
    def testDecimalToRoman_XXI(self):
        result = decimalToRoman(35)
        self.assertEqual(result, 'XXXV')
    def testDecimalToRoman_XXII(self):
        result = decimalToRoman(76)
        self.assertEqual(result, 'LXXVI')
    def testDecimalToRoman_XXIII(self):
        result = decimalToRoman(89)
        self.assertEqual(result, 'LXXXIX')
    def testDecimalToRoman_XXIV(self):
        result = decimalToRoman(80)
        self.assertEqual(result, 'LXXX')
    def testDecimalToRoman_XXV(self):
        result = decimalToRoman(186)
        self.assertEqual(result, 'CLXXXVI')
    def testDecimalToRoman_XXVI(self):
        result = decimalToRoman(1286)
        self.assertEqual(result, 'MCCLXXXVI')
    def testDecimalToRoman_XXVII(self):
        result = decimalToRoman(2286)
        self.assertEqual(result, 'MMCCLXXXVI')
    def testDecimalToRoman_XXVII(self):
        result = decimalToRoman(1119)
        self.assertEqual(result, 'MCXIX')
    def testDecimalToRoman_XXVIII(self):
        result = decimalToRoman(46)
        self.assertEqual(result, 'XLVI')
    def testDecimalToRoman_XXIX(self):
        result = decimalToRoman(999)
        self.assertEqual(result, 'CMXCIX')
    def testDecimalToRoman_XXX(self):
        result = decimalToRoman(305)
        self.assertEqual(result, 'CCCV')
    def testDecimalToRoman_XXXI(self):
        result = decimalToRoman(447)
        self.assertEqual(result, 'CDXLVII')
    def testDecimalToRoman_XXXII(self):
        result = decimalToRoman(667)
        self.assertEqual(result, 'DCLXVII')
    def testDecimalToRoman_XXXIII(self):
        result = decimalToRoman(996)
        self.assertEqual(result, 'CMXCVI')
    def testDecimalToRoman_XXXIV(self):
        result = decimalToRoman(886)
        self.assertEqual(result, 'DCCCLXXXVI')
    def testDecimalToRoman_XXXVI(self):
        result = decimalToRoman(86)
        self.assertEqual(result, 'LXXXVI')
    def testDecimalToRoman_XXXVII(self):
        result = decimalToRoman(85)
        self.assertEqual(result, 'LXXXV')

    
class TestRomanToDecimal(unittest.TestCase):

    def testRomanToDecimal_I(self):
        result = romanToDecimal('I')
        self.assertEqual(result, 1)
    def testRomanToDecimal_II(self):
        result = romanToDecimal('II')
        self.assertEqual(result, 2)
    def testRomanToDecimal_III(self):
        result = romanToDecimal('IV')
        self.assertEqual(result, 4)
    def testRomanToDecimal_IV(self):
        result = romanToDecimal('V')
        self.assertEqual(result, 5)
    def testRomanToDecimal_V(self):
        result = romanToDecimal('VI')
        self.assertEqual(result, 6)
    def testRomanToDecimal_VI(self):
        result = romanToDecimal('IX')
        self.assertEqual(result, 9)
    def testRomanToDecimal_VII(self):
        result = romanToDecimal('X')
        self.assertEqual(result, 10)
    def testRomanToDecimal_VIII(self):
        result = romanToDecimal('XXXVI')
        self.assertEqual(result, 36)
    def testRomanToDecimal_IX(self):
        result = romanToDecimal('XLI')
        self.assertEqual(result, 41)
    def testRomanToDecimal_X(self):
        result = romanToDecimal('XLVII')
        self.assertEqual(result, 47)
    def testRomanToDecimal_XI(self):
        result = romanToDecimal('XCVIII')
        self.assertEqual(result, 98)
    def testRomanToDecimal_XII(self):
        result = romanToDecimal('LVI')
        self.assertEqual(result, 56)
    def testRomanToDecimal_XIII(self):
        result = romanToDecimal('LXXVII')
        self.assertEqual(result, 77)
    def testRomanToDecimal_XIV(self):
        result = romanToDecimal('CXXIII')
        self.assertEqual(result, 123)
    def testRomanToDecimal_XV(self):
        result = romanToDecimal('CCXLV')
        self.assertEqual(result, 245)
    def testRomanToDecimal_XVI(self):
        result = romanToDecimal('CCCXXXIII')
        self.assertEqual(result, 333)
    def testRomanToDecimal_XVII(self):
        result = romanToDecimal('CDLIX')
        self.assertEqual(result, 459)
    def testRomanToDecimal_XVIII(self):
        result = romanToDecimal('CMXCIX')
        self.assertEqual(result, 999)
    def testRomanToDecimal_XIX(self):
        result = romanToDecimal('DCLXVI')
        self.assertEqual(result, 666)
    def testRomanToDecimal_XX(self):
        result = romanToDecimal('MDXVII')
        self.assertEqual(result, 1517)
    def testRomanToDecimal_XX(self):
        result = romanToDecimal('MMLXXVII')
        self.assertEqual(result, 2077)
    
    
    



if __name__ == '__main__':
    unittest.main()

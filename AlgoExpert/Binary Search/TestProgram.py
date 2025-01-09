#Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to find if the target number is contained in the array and should return its index if it is, otherwise -1.

# Add, edit, or remove tests in this file.
# Treat it as your playground!

'''
Utiliza el módulo unittest de Python para definir y ejecutar estas pruebas.
Cada método test_case_X dentro de la clase TestProgram es una prueba individual que verifica si la función binarySearch 
devuelve el resultado esperado para un conjunto específico de entradas.
Por ejm.: self.assertEqual(program.binarySearch([1, 5, 23, 111], 5), 1) verifica si la función binarySearch devuelve 1
'''
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.binarySearch([1, 5, 23, 111], 111), 3)#3

    def test_case_2(self):
        self.assertEqual(program.binarySearch([1, 5, 23, 111], 5), 1)

    def test_case_3(self):
        self.assertEqual(program.binarySearch([1, 5, 23, 111], 35), -1)

    def test_case_4(self):
        self.assertEqual(
            program.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3
        )

    def test_case_5(self):
        self.assertEqual(
            program.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 72), 8
        )

    def test_case_6(self):
        self.assertEqual(
            program.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 73), 9
        )

    def test_case_7(self):
        self.assertEqual(
            program.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 70), -1
        )

    def test_case_8(self):
        self.assertEqual(
            program.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 355), 10
        )

    def test_case_9(self):
        self.assertEqual(
            program.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 354), -1
        )
   
if __name__ == "__main__":
    unittest.main()


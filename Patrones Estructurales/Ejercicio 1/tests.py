import unittest
import os
from pizza_menucomponente import Pizza
from bebida_menucomponente import Bebida
from postre_menucomponente import Postre
from combo_pareja import ComboPareja
from basico_menu import Basico

class TestMenuComponente(unittest.TestCase):

    def setUp(self):
        self.pizza = Pizza("Pizza de Pepperoni", 8.00)
        self.bebida = Bebida("Refresco de Cola", 2.00)
        self.postre = Postre("Tarta de Chocolate", 3.50)
        self.combo_pareja = ComboPareja("Pizza Margarita", "Pizza Hawaiana", "Agua", "Helado")
        self.basico = Basico("Pizza Vegetariana", "Refresco de Limón", "Brownie")

    def tearDown(self):
        if os.path.exists("Patrones Estructurales/Ejercicio 1/data/pizza_cliente.csv"):
            os.remove("Patrones Estructurales/Ejercicio 1/data/pizza_cliente.csv")

    def test_precio_pizza(self):
        self.assertEqual(self.pizza.precio(), 8.00)

    def test_operacion_pizza(self):
        self.assertEqual(self.pizza.operacion(), "Pizza de Pepperoni: 8.0.")

    def test_precio_bebida(self):
        self.assertEqual(self.bebida.precio(), 2.00)

    def test_operacion_bebida(self):
        self.assertEqual(self.bebida.operacion(), "Refresco de Cola: 2.0.")

    def test_precio_postre(self):
        self.assertEqual(self.postre.precio(), 3.50)

    def test_operacion_postre(self):
        self.assertEqual(self.postre.operacion(), "Tarta de Chocolate: 3.5.")

    def test_precio_combo_pareja(self):
        self.assertEqual(self.combo_pareja.precio(), 17.75)

    def test_operacion_combo_pareja(self):
        expected_output = "Menú Combo pareja:\n Pizza Margarita: 7.0., Pizza Hawaiana: 7.0., Agua: 1.5., Helado: 2.25."
        self.assertEqual(self.combo_pareja.operacion(), expected_output)

    def test_precio_basico(self):
        self.assertEqual(self.basico.precio(), 10.75)

    def test_operacion_basico(self):
        expected_output = "Menú Básico:\n Pizza Vegetariana: 7.0., Refresco de Limón: 1.5., Brownie: 2.25."
        self.assertEqual(self.basico.operacion(), expected_output)

    def test_agregar_csv(self):
        self.combo_pareja.agregar_csv()
        with open("Patrones Estructurales/Ejercicio 1/data/pizza_cliente.csv", newline="") as archivo:
            row = archivo.readlines()[-1]
            expected_row = "Pizza Margarita,Pizza Hawaiana,Agua,Helado\r\n"
            self.assertEqual(row, expected_row)

if __name__ == '__main__':
    unittest.main()
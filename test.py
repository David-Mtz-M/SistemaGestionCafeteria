# Test Cases del Sistema de Gestión de Cafetería 
# Programador: David Martínez Molina  A01735425

import unittest

from gestionBebidas import addBebida

class TestAddBebida(unittest.TestCase):
    
    # Caso de prueba 1: Nombre del artículo alfabético (válido)
    def test_nombre_alfabetico_valido(self):
        self.assertTrue(addBebida("Café,10"))
    
    # Caso de prueba 2: Nombre del artículo con menos de 2 caracteres de longitud (inválido)
    def test_nombre_corto_invalido(self):
        self.assertFalse(addBebida("T,10"))
    
    # Caso de prueba 3: Nombre del artículo con 2 a 15 caracteres de longitud (válido)
    def test_nombre_longitud_valida(self):
        self.assertTrue(addBebida("Café con Leche,10"))
    
    # Caso de prueba 4: Valor del tamaño en el rango de 1 a 48 (válido)
    def test_tamano_rango_valido(self):
        self.assertTrue(addBebida("Té,1,10,20,30"))
    
    # Caso de prueba 5: Valor del tamaño no es un número entero (inválido)
    def test_tamano_entero_invalido(self):
        self.assertFalse(addBebida("Café,1.5"))
    
    # Caso de prueba 6: Valores del tamaño en orden ascendente (válido)
    def test_tamano_orden_valido(self):
        self.assertTrue(addBebida("Té,1,2,4,8,16"))
    
    # Caso de prueba 7: Se ingresan de uno a cinco valores de tamaño (válido)
    def test_cantidad_tamanos_valida(self):
        self.assertTrue(addBebida("Cappuccino,1,2"))
    
    # Caso de prueba 8: Nombre del artículo es el primero en la entrada (válido)
    def test_nombre_primero_valido(self):
        self.assertTrue(addBebida("Latte,12,24"))
    
    # Caso de prueba 9: Una sola coma separa cada entrada en la lista (válido)
    def test_coma_separacion_valida(self):
        self.assertTrue(addBebida("Mocha,12,24,36,48"))
    
    # Caso de prueba 10: La entrada contiene espacios en blanco (válido)
    def test_espacios_en_blanco_validos(self):
        self.assertTrue(addBebida("Frappé, 1, 2, 4, 8, 16"))
    
    # Caso de prueba 11: La entrada no contiene espacios en blanco (válido)
    def test_sin_espacios_en_blanco_validos(self):
        self.assertTrue(addBebida("Té,1,2,4,8,16"))

if __name__ == '__main__':
    unittest.main()

 
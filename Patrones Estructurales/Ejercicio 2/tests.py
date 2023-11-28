import unittest
from unittest.mock import patch
from real_subject import RealSubject
from proxy import Proxy
from documento import Documento
from enlace import Enlace
from carpeta import Carpeta


class TestTuModulo(unittest.TestCase):

    def setUp(self):
        # Crea instancias necesarias para las pruebas
        self.real_subject = RealSubject("Nombre", "Apellido", "12345678Y")
        self.proxy = Proxy(self.real_subject)

    def test_proxy_request_without_access(self):
        # Prueba para el método request de Proxy sin acceso
        with patch.object(self.proxy, 'check_access', return_value=False):
            with patch("builtins.print") as mock_print:
                output = self.proxy.request()
                mock_print.assert_not_called()
                self.assertEqual(output, False)

    def test_documento_add_without_access(self):
        # Prueba para el método add de Documento sin acceso
        documento = Documento("Test", "Contenido", "Texto", 10, sensible=True)
        with patch("builtins.print") as mock_print:
            with patch("builtins.input", side_effect=["Nombre", "Apellido", "12345678Y"]):
                documento.add("Nuevo contenido")
                mock_print.assert_called_with("No puede modificar el documento si no ha registrado su acceso previamente.")
                self.assertEqual(documento._contenido, "Contenido")

    def test_enlace_access(self):
        # Prueba para el método access de Enlace
        enlace = Enlace("/ruta/al/enlace")
        self.assertEqual(enlace.access(), "/ruta/al/enlace")

    def test_carpeta_add(self):
        # Prueba para el método add de Carpeta
        carpeta = Carpeta("Carpeta")
        documento = Documento("Documento", "Contenido", "Texto", 10)
        carpeta.add(documento)
        self.assertIn(documento, carpeta._children)

    def test_carpeta_remove(self):
        # Prueba para el método remove de Carpeta
        carpeta = Carpeta("Carpeta")
        documento = Documento("Documento", "Contenido", "Texto", 10)
        carpeta.add(documento)
        carpeta.remove(documento)
        self.assertNotIn(documento, carpeta._children)

    def test_carpeta_access(self):
        # Prueba para el método access de Carpeta
        carpeta = Carpeta("Carpeta")
        documento = Documento("Documento", "Contenido", "Texto", 10)
        carpeta.add(documento)
        self.assertEqual(carpeta.access(), ["Archivo Documento"])


if __name__ == '__main__':
    unittest.main()
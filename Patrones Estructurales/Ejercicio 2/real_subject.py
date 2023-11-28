from log import log
from subject import Subject

class RealSubject(Subject):
    def __init__(self, nombre, apellido, dni) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

    @log('Patrones Estructurales/Ejercicio 2/accesos/registro_accesos.log')
    def request(self) -> None:
        '''
        Si el usuario hace una petición, se mostrará su nombre, apellido y dni.
        '''
        return [self._nombre, self._apellido, self._dni] 
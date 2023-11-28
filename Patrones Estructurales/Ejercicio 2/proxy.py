from abc import ABC, abstractmethod
from log import log

class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    def __init__(self, nombre, apellido, dni) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

    @log('accesos/registro_accesos.log')
    def request(self) -> None:
        '''
        Si el usuario hace una petición, se mostrará su nombre, apellido y dni.
        '''
        return [self._nombre, self._apellido, self._dni] 


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")
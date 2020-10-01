from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFactory(ABC):

    """
    La interfaz AbstractFactory declara conjunto de metodos que devuelven los
    prductos abstractos. Estos se denominan familia y se relacionan por un tema
    o concepto de alto nivel.
    Los productos de una familia pueden colaborar entre ellos

    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):

    """
    Las ConcreteFactory producen una familia de productos que
    pertenecen a un solo variante. La fabrica garantiza que los
    prductos sean compatibles.
    Cada Factory tiene una variable de producto correspondiente

    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):


    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

class AbstractProductA(ABC):

    """
    Cada producto en la familia debe de tener su interfaz.
    Cada variable del producto implementa la interfaz que le corresponde

    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "El resultado de un producto A1"

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "El resultado de un producto A2"

class AbstractProductB(ABC):

    """
    Interfaz base del producto B
    Todos los productos pueden interactuar entre si, pero la interaccion
    adecuada solo es posible entre productos de una misma variable.

    """

    @abstractmethod
    def useful_function_b(self) -> None:
        """ El producto B puede poseer sus propios metodos"""
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """ Y puede colaborar con el ProductoA.
            Por ser creados desde la misma AbstractFactory esto nos asegura
            que todos los productos que se crean sean compatibles  """
        pass



class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "El resultado de un producto B1"

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"El resultado de la colaboracion de B1 con ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "El resultado de un producto B2"

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f"El resultado de la colaboracion de B2 con ({result})"

def client_code(factory: AbstractFactory) -> None:

    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")

if __name__ == "__main__":

    print("\n")

    print("Cliente: Probando el codigo del cliente con el primer tipo de fabrica: ")
    client_code(ConcreteFactory1())

    print("\n")

    print("Cliente: Probando el mismo cliente con el segundo tipo de fabrica: ")
    client_code(ConcreteFactory2())

    print("\n")
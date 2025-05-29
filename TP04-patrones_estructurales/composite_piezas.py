from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """

        pass


class Leaf(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


# Clases específicas para la estructura solicitada
class Pieza(Leaf):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def operation(self) -> str:
        return f"Pieza({self.nombre})"


class SubConjunto(Composite):
    def __init__(self, nombre: str):
        super().__init__()
        self.nombre = nombre

    def operation(self) -> str:
        results = [child.operation() for child in self._children]
        return f"SubConjunto({self.nombre}:[{', '.join(results)}])"


class ProductoPrincipal(Composite):
    def __init__(self, nombre: str):
        super().__init__()
        self.nombre = nombre

    def operation(self) -> str:
        results = [child.operation() for child in self._children]
        return f"ProductoPrincipal({self.nombre}:[{', '.join(results)}])"


def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Thanks to the fact that the child-management operations are declared in the
    base Component class, the client code can work with any component, simple or
    complex, without depending on their concrete classes.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)

    # Crear el producto principal
    producto = ProductoPrincipal("ProductoX")
    # Crear 3 subconjuntos con 4 piezas cada uno
    for i in range(1, 4):
        subconjunto = SubConjunto(f"SubConjunto{i}")
        for j in range(1, 5):
            subconjunto.add(Pieza(f"P{i}{j}"))
        producto.add(subconjunto)
    print("Estructura inicial del ensamblado:")
    print(producto.operation())
    print()
    # Agregar subconjunto opcional
    subconjunto_opcional = SubConjunto("SubConjuntoOpcional")
    for k in range(1, 5):
        subconjunto_opcional.add(Pieza(f"O{k}"))
    producto.add(subconjunto_opcional)
    print("Estructura con subconjunto opcional:")
    print(producto.operation())
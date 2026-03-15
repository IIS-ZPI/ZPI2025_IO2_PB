from abc import ABC, abstractmethod


class IArithmeticsAdd(ABC):
    @abstractmethod
    def addition(self, A: float, B: float) -> float:
        pass


class IArithmeticsDiff(ABC):
    @abstractmethod
    def difference(self, A: float, B: float) -> float:
        pass


class IArithmeticsMult(ABC):
    @abstractmethod
    def multiplication(self, A: float, B: float) -> float:
        pass


class IArithmeticsDiv(ABC):
    @abstractmethod
    def division(self, A: float, B: float) -> float:
        pass


class IArithmeticsPow(ABC):
    @abstractmethod
    def power(self, A: float, B: float) -> float:
        pass
    


class ArithmeticsDiff(IArithmeticsDiff):
    def difference(self, A: float, B: float) -> float:
        return A - B


class ArithmeticsAdd(IArithmeticsAdd):
    def addition(self, A: float, B: float) -> float:
        return A + B

#comment 1 krzysztoftomczyk23
class ArithmeticsMult(IArithmeticsMult):
    def multiplication(self, A: float, B: float) -> float:
        return A * B

     
class ArithmeticsDiv(IArithmeticsDiv):
    def division(self, A: float, B: float) -> float:
        if B == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return A / B


class ArithmeticsPow(IArithmeticsPow):
    def power(self, A: float, B: float) -> float:
        return A ** B

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

class ArithmeticsMult(IArithmeticsMult):
    def multiplication(self, A: float, B: float) -> float:
        return A * B
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

#comment1 - 251240
class ArithmeticsAdd(IArithmeticsAdd):
    #comment2 - 251240
    def addition(self, A: float, B: float) -> float:
        #comment3 - 251240
        return A + B

#comment 1 krzysztoftomczyk23
class ArithmeticsMult(IArithmeticsMult):
    #comment 2 krzysztoftomczyk23
    def multiplication(self, A: float, B: float) -> float:
        #comment 3 krzysztoftomczyk23
        return A * B

     
class ArithmeticsDiv(IArithmeticsDiv):
    def division(self, A: float, B: float) -> float:
        if B == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return A / B

#comment1-ksaletra
class ArithmeticsPow(IArithmeticsPow):
    #comment2 - ksaletra
    def power(self, A: float, B: float) -> float:
        #comment3 - ksaletra
        return A ** B

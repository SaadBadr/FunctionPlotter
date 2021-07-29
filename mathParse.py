class MathExpression:
    def __init__(self, exp, x) -> None:
        self.x = x
        self.exp = exp
        modifiedExp = exp.casefold().replace(" ", "").replace("-", "+-1*")
        self.y = self.__evaluateAddition(modifiedExp)

    def __strValueConv(self, str):
        output = None
        countDot = str.count(".")

        if str == "x":
            output = self.x.copy()
        elif countDot > 1:
            print("DOT ERROR")
        elif countDot == 1:
            output = float(str)
        else:
            output = int(str)

        return output

    def __evaluateSingles(self, exp):
        list = exp.split("^")
        output = self.__strValueConv(list[0])
        size = len(list)

        for i in range(1, size):
            output = pow(output, self.__strValueConv(list[i]))

        return output

    def __evaluateDivision(self, exp):
        list = exp.split("/")
        output = self.__evaluateSingles(list[0])
        size = len(list)

        for i in range(1, size):
            output /= self.__evaluateSingles(list[i])

        return output

    def __evaluateMultiplication(self, exp):
        list = exp.split("*")
        output = 1
        for e in list:
            output *= self.__evaluateDivision(e)

        return output

    def __evaluateAddition(self, exp):
        list = exp.split("+")
        output = 0
        for e in list:
            output += self.__evaluateMultiplication(e)
        return output

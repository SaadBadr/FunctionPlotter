import re


class MathExpression:
    def __init__(self, exp, x) -> None:
        self.exp_dict = {'x': x}
        self.exp = exp
        self.y = self.__evaluate()

    def __strValueConv(self, str):
        output = None
        countDot = str.count(".")

        if re.match(r'[xz][0-9]*', str) is not None:
            output = self.exp_dict[str].copy()
        # elif countDot > 1:
        #     print("DOT ERROR")
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

    def __evaluateBrackets(self, exp):

        inner_pattern = r"\(([x0-9\*\+\-\/\^]*)\)"

        while True:

            inner_level_brackets = re.findall(
                string=exp, pattern=inner_pattern)

            if len(inner_level_brackets) < 1:
                return exp
            current_idx = len(self.exp_dict)

            for value in inner_level_brackets:
                exp = exp.replace(f'({value})', f'z{current_idx}')
                self.exp_dict[f'z{current_idx}'] = self.__evaluateAddition(
                    value)
                current_idx += 1

    def __evaluate(self):
        modifiedExp = self.exp.casefold().replace(" ", "").replace("-", "+-1*")
        evaluatedBracketsExp = self.__evaluateBrackets(modifiedExp)
        return self.__evaluateAddition(evaluatedBracketsExp)

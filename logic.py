# https://github.com/alisoltanirad/Logic.git

class Sentence:

    def __invert__(self):
        return Invert(self)

    def __and__(self, other):
        return Conjunction(self, other)

    def __or__(self, other):
        return Disjunction(self, other)

    def __gt__(self, other):
        return Implication(self, other)

    def __eq__(self, other):
        return Equality(self, other)


class BinarySentence(Sentence):

    def __init__(self, lchild, rchild):
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self):
        return '(' + self.lchild + ' ' + self.operator + ' ' + self.rchild +  ')'


class Atomic(Sentence):
    pass


class Invert(Sentence):
    pass


class Conjunction(BinarySentence):
    operator = '∧'


class Disjunction(BinarySentence):
    operator = '∨'


class Implication(BinarySentence):
    operator = '→'


class Equality(BinarySentence):
    operator = '↔'


def main():
    pass


if __name__ == '__main__':
    main()
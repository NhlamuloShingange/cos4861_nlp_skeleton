
class Span:
    """
    Span objects are used to define boundaries within other iterables.
    """
    def __init__(self, start, end):
        if not start <= end:
            raise ValueError('Start cannot be greater than or equal to End')

        self._start = start
        self._end = end

    @property
    def span(self):
        """
        Return the span start and end scalars
        :return: The start and end indexes
        """
        return self._start, self._end

    def __eq__(self, other):
        start, fin = other.span()
        return self._start == start and self._end == fin


class DistanceCalculator:
    """
    The ADistanceCalculator class defines a metric on strings. It is a way of determining the distance from
    one string to another.
    """

    def __init__(self, insert_cost=1, deletion_cost=1, subst_cost=1):
        """
        The constructor for the distance calculator. The insert, deletion, and substitution cost can be specified
        as state for the object.
        :param insert_cost:
        :param deletion_cost:
        :param subst_cost:
        """
        self._insert_cost = insert_cost
        self._deletion_cost = deletion_cost
        self._subst_cost = subst_cost

    def distance(self, source, target):
        """
        Calculates the distance between two strings.
        :param t:
        :param s:
        :param source: The source string
        :param target: The target string
        :return: The scalar distance between the source and target.
        """
        s = len(source)
        t = len(target)
        table = [[0 for j in range(s + 1)] for i in range(t + 1)]

        for i in range(t + 1):
            table[i][0] = i

        for j in range(s + 1):
            table[0][j] = j

        for i in range(1, t + 1):
            for j in range(1, s + 1):
                if source[j-self._deletion_cost] == target[i-self._deletion_cost]:
                    table[i][j] = table[i-self._deletion_cost][j-self._deletion_cost]
                else:
                    table[i][j] = min([table[i-self._insert_cost][j],
                                       table[i][j-self._deletion_cost],
                                       table[i-self._subst_cost][j-self._subst_cost]]) + 1

        return table[len(target)][len(source)]

        raise NotImplementedError('Distance calculation not implemented yet')


test = DistanceCalculator()
s = input("Enter first word : ")
t = input("Enter second word : ")
result = test.distance(s, t)
print(result)

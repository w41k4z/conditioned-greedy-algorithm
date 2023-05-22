class NumberArray:

    @staticmethod
    def dichotomous_search(n, arr=[], is_sorted=False):
        if n is None:
            raise Exception("The target 'n' is not defined")

        if len(arr) == 0:
            return None

        elements = sorted(arr) if not is_sorted else arr

        if len(elements) == 1:
            return 0 if elements[0] == n else None

        middle = len(elements) // 2

        if elements[middle] == n:
            return middle

        if elements[middle] > n:
            return NumberArray.dichotomous_search(n, elements[:middle], True)
        else:
            result = NumberArray.dichotomous_search(
                n, elements[middle+1:], True)
            return middle + 1 + result if result is not None else None

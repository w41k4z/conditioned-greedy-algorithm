from number_array import NumberArray


class ConditionnedGlutton:

    # T: the sum T
    # arr: the array of the elements
    # n: the number of combinaison
    def solve(self, T, arr, n, is_sorted):
        # the array must be sorted for the dichotomous search
        elements = sorted(arr) if not is_sorted else arr

        # initial glutton algo
        if n is None:
            for i in range(1, len(elements) + 1):
                result = self.glutton_search(T, elements, i)
                if result is not None:
                    return result
            return None
        # conditionned glutton (n is specified)
        else:
            return self.glutton_search(T, elements, n)

    # core method solving
    def glutton_search(self, T, arr=[], n=1):
        if T is None:
            raise Exception("The target 'T' is not defined")

        # This refers to the basic find() method
        if n == 1:
            element_index = NumberArray.dichotomous_search(T, arr, True)
            return arr[element_index] if element_index is not None else None

        # This is the main purpose of this method
        # Here we can solve the search
        elif n == 2:
            for index in range(len(arr)):
                header = arr[index]

                # no need to continue the search if the last element + the header is less than T
                if header + arr[-1] < T:
                    continue
                # As the array is sorted, there is no solution if this condition is true
                if header > T or header + arr[index + 1] > T:
                    return None

                tail_coupled_index = NumberArray.dichotomous_search(
                    T - header, arr[index+1:], True)
                if tail_coupled_index is not None:
                    return [header] + [arr[tail_coupled_index + index + 1]]
            return None

        # This case will recursively be redirected to the above step to be solved
        else:
            for index in range(len(arr)):
                header = arr[index]
                remains = self.glutton_search(
                    T - header, arr[index+1:], n - 1)
                if remains is not None:
                    return [header] + remains
            return None

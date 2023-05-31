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

    def glutton_search(self, T, arr=[], n=1):
        if T is None:
            raise Exception("The target 'T' is not defined")

        # This refers to the basic find() method
        if n == 1:
            for element in arr:
                if element == T:
                    return [element]
            return None

        # This is the main purpose of this method
        # Here we can solve the search
        elif n == 2:
            for index in range(len(arr)):
                header = arr[index]
                couple_index = NumberArray.dichotomous_search(
                    T - header, arr[index+1:], True)
                if couple_index is not None:
                    return [header] + [arr[couple_index+index+1]]
            return None

        # This part will recursively be redirected to the above step to be solved
        else:
            for index in range(len(arr)):
                header = arr[index]
                remains = self.glutton_search(
                    T - header, arr[index+1:], n - 1)
                if remains is not None:
                    return [header] + remains
            return None

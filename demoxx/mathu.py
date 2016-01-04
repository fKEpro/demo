
class Mathu:
    def __init__(self):
        print('call __init__ from Mathu class')

    def add(self, num_a, num_b):
        return num_a + num_b

    def div(self, num_a, num_b):
        try:
            result = num_a / num_b
        except ZeroDivisionError as e:
            raise e

        return result

    def check_even(self, number):
        return number % 2 == 0


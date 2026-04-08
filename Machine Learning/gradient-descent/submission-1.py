class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        minimizer = init
        for _ in range(iterations):
            deriv = 2*minimizer
            minimizer -= learning_rate*deriv
        return round(minimizer,5)

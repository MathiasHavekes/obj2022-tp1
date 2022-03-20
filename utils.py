class Utils:
    """
    Fonction de type : y = ax + b
    On trouve a avec les points extremes :
    a = (y_b - y_a) / (x_b - x_a)
    b = -(ax - y)
    """
    def castValue(x: int, y_a: int, y_b: int, x_a: int, x_b: int) -> int:
        gradient = (y_b - y_a) / (x_b - x_a)

        intercept = - (gradient * x_b - y_b)

        return round(gradient * x + intercept)

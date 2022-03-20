class Utils:
    """
    Fonction de type : y = ax + b
    On trouve a avec les points extremes :
    a = (y_b - y_a) / (x_b - x_a)
    b = -(ax - y)
    """
    def castToPercentage(distance, max_value, min_value) -> int:
        gradient = 100 / (max_value - min_value)

        intercept = - (gradient * max_value - 100)

        return round(gradient * distance + intercept)

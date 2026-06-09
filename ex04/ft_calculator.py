class calculator:
    """A class that is able to do calculations of a vector with a scalar"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Makes the dot product of the stored vector with another one"""
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]

        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds a vector to the stored one"""
        result = []
        for i in range(len(V1)):
            result.append(float(V1[i] + V2[i]))

        print(f"Dot product is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substracts a vector from the stored one"""
        result = []
        for i in range(len(V1)):
            result.append(float(V1[i] - V2[i]))

        print(f"Dot product is: {result}")

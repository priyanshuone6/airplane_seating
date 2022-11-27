class AirplaneSeating:
    """
    Write here
    """

    def __init__(self, nested_arr, passengers):
        self.nested_arr = nested_arr
        self.passengers = passengers

    def build_layout(self):
        layout = []
        # Create a matrix from the nested array
        for arr in self.nested_arr:
            cols, rows = arr

            # Initialize the matrix with -1
            matrix = []
            for _ in range(rows):
                matrix.append([-1] * cols)
            layout.append(matrix)

        return layout

    def assign_aisle_seats(self, layout):

        self.seat_number = 1

        for i in range(len(layout)):
            # Parse through the nested list
            for j in range(len(layout[i])):

                # Set the first and last elements to a aisle seat
                layout[i][j][0] = f"{self.seat_number} Aisle"
                self.seat_number += 1
                layout[i][j][-1] = f"{self.seat_number} Aisle"
                self.seat_number += 1

                if self.seat_number == self.passengers:
                    break

        return layout

    def assign_window_seats(self, layout):

        for i in range(len(layout)):
            # Parse through the nested list
            for j in range(len(layout[i])):

                # Override the first and last element of the nested list to a window seat
                if i == 0:
                    layout[0][j][0] = f"{self.seat_number} Window"
                    self.seat_number += 1
                if i == len(layout) - 1:
                    layout[-1][j][-1] = f"{self.seat_number} Window"
                    self.seat_number += 1

                if self.seat_number == self.passengers:
                    break

        return layout

    def assign_middle_seats(self, layout):

        for i in range(len(layout)):
            # Parse through the nested list
            for j in range(len(layout[i])):

                # Set the elements between the index 0 and -1 to a middle seat
                for k in range(1, len(layout[i][j]) - 1):
                    layout[i][j][k] = f"{self.seat_number} Middle"
                    self.seat_number += 1

                    if self.seat_number == self.passengers:
                        break

        return layout


def main(input_array, input_passengers):
    """Function to run the program"""
    airplane_class = AirplaneSeating(input_array, input_passengers)
    layout_func = airplane_class.build_layout()
    aisle_func = airplane_class.assign_aisle_seats(layout_func)
    window_func = airplane_class.assign_window_seats(aisle_func)
    middle_func = airplane_class.assign_middle_seats(window_func)

    return middle_func


if __name__ == "__main__":
    input_array = [[3, 2], [4, 3], [2, 3], [3, 4]]
    input_passengers = 30

    print(main(input_array, input_passengers))

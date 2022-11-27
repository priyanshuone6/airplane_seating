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

    def assign_seats(self, layout):

        for i in range(len(layout)):
            # Parse through the nested list
            for j in range(len(layout[i])):

                # Set the elements between the index 0 and -1 to a middle seat
                for k in range(1, len(layout[i][j]) - 1):
                    layout[i][j][k] = "Middle"

                # Set the first and last elements to a aisle seat
                layout[i][j][0] = "Aisle"
                layout[i][j][-1] = "Aisle"

                # Override the first and last element of the nested list to a window seat
                if i == 0:
                    layout[0][j][0] = "Window"
                if i == len(layout) - 1:
                    layout[-1][j][-1] = "Window"

        return layout

    #def assign_seat_number(self, layout):
    #   for seat in layout[0]:
    #       print(seat)


if __name__ == "__main__":
    input_array = [[3, 2], [4, 3], [2, 3], [3, 4]]
    input_passengers = 30

    airplane_class = AirplaneSeating(input_array, input_passengers)
    layout_func = airplane_class.build_layout()
    seats_func = airplane_class.assign_seats(layout_func)
    #seat_num_func = airplane_class.assign_seat_number(seats_func)

    print(seats_func)

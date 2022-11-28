class Airplane:
    """
    It helps seat audiences in a flight by seating passengers starting from the
    front row to the back, starting from the left to the right, and filling
    the aisle seats first, followed by window seats, followed by centre seats.
    """

    def __init__(self, dims, num_passengers):
        self.dims = dims
        self.num_passengers = num_passengers
        self._layout = []

        # Initialize the seat number
        self.seat_number = 1

        # Raise an error if the array or passengers is empty
        if not self.dims:
            raise ValueError("Array cannot be empty")
        if not self.num_passengers:
            raise ValueError("Passengers cannot be empty")

        # Raise an error if array is not a list
        if not isinstance(self.dims, list):
            raise TypeError("Given dimensions must be a list")

        # Raise an error if passengers is not an integer
        if not isinstance(self.num_passengers, int):
            raise TypeError("Passengers must be an integer")

        # Raise an error if passengers are negative
        if self.num_passengers < 0:
            raise ValueError("Passengers cannot be negative")

    def __str__(self):
        """Pretty print the airport layout with passengers."""
        # get the length of the biggest passenger number to properly indent everything
        indent = len(str(self.num_passengers))
        max_len = max(map(len, self.layout))
        layout_heading = 'Airplane Layout'
        seating_rows = [layout_heading, '=' * len(layout_heading)]
        for row_idx in range(max_len):

            row_str = []
            for arr in self.layout:
                if row_idx < len(arr):
                    arr_row = [f'{num:<{indent}}' for num in arr[row_idx]]
                else:
                    arr_row = [' ' * indent for _ in range(len(arr[0]))]
                row_str.append(' '.join(arr_row))

            # Add 2 extra spaces between seat groups than the length of the biggest passenger num
            seating_rows.append((' ' * (indent + 2)).join(row_str))

        return '\n'.join(seating_rows)

    def _build_layout(self):
        """
        Builds the layout of the flight from the input array by initializing
        matrix with 0.
        """
        # Create a matrix from the nested array
        for arr in self.dims:
            cols, rows = arr
            # Initialize the matrix with 0
            matrix = [[0] * cols for _ in range(rows)]
            self._layout.append(matrix)

    @property
    def layout(self):
        """Layout of the airplane."""
        if not self._layout:
            self._build_layout()

        return self._layout

    def assign_aisle_seats(self):
        """Assigns the aisle seats to the passengers."""
        for i in range(len(self.layout)):
            # Parse through the nested list
            for j in range(len(self.layout[i])):

                # Skip window seats
                if not (i == 0 and i == 1):
                    # Set first and last elements of sub list to a aisle seat
                    self.layout[i][j][0] = f"{self.seat_number} Aisle"
                    self.seat_number += 1
                    self.layout[i][j][-1] = f"{self.seat_number} Aisle"
                    self.seat_number += 1

                    if self.seat_number == self.num_passengers:
                        break

    def assign_window_seats(self):
        """Assigns the window seats to the passengers."""
        for i in range(len(self.layout)):
            # Parse through the nested list
            for j in range(len(self.layout[i])):

                # Set first and last element of the nested list to a window seat
                if i == 0:
                    self.layout[0][j][0] = f"{self.seat_number} Window"
                    self.seat_number += 1
                if i == len(self.layout) - 1:
                    self.layout[-1][j][-1] = f"{self.seat_number} Window"
                    self.seat_number += 1

                if self.seat_number == self.num_passengers:
                    break

    def assign_middle_seats(self):
        """Assigns the middle seats to the passengers."""
        for i in range(len(self.layout)):
            # Parse through the nested list
            for j in range(len(self.layout[i])):
                # Set the elements between the index 0 and -1 to a middle seat
                for k in range(1, len(self.layout[i][j]) - 1):
                    self.layout[i][j][k] = f"{self.seat_number} Middle"
                    self.seat_number += 1

                    if self.seat_number == self.num_passengers:
                        break


def main(input_array, input_passengers):
    """Function to run the program."""
    airplane = Airplane(input_array, input_passengers)
    airplane.assign_aisle_seats()
    airplane.assign_window_seats()
    airplane.assign_middle_seats()
    return airplane


if __name__ == "__main__":
    input_array = [[3, 2], [4, 3], [2, 3], [3, 4]]
    input_passengers = 30

    print(main(input_array, input_passengers))

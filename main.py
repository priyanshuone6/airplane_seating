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
        self.passengers_seated = 0

        # Raise an error if array is not a list
        if not isinstance(self.dims, list):
            raise TypeError("Given dimensions must be a list")

        if len(self.dims) == 0:
            raise ValueError("Airplane must have some seats")

        # Raise an error if dims is not proper
        for item in self.dims:
            if not isinstance(item, list) or len(item) != 2:
                raise ValueError(
                    f"Expected dims to contain arrays of length 2, got '{item}'")

        # Raise an error if passengers is not an integer
        if not isinstance(self.num_passengers, int):
            raise TypeError("Passengers must be an integer")

        # Raise an error if passengers are negative
        if self.num_passengers < 0:
            raise ValueError("Passengers cannot be negative")

        total_capacity = sum([dim[0] * dim[1] for dim in self.dims])
        if self.num_passengers > total_capacity:
            raise ValueError(
                f"Plane doesn't have enough seats for {self.num_passengers} passengers")

    def __str__(self):
        """Pretty print the airport layout with passengers."""
        # get the length of the biggest passenger number to properly indent everything
        indent = len(str(self.num_passengers))
        layout_heading = 'Airplane Layout'
        seating_rows = [layout_heading, '=' * len(layout_heading)]
        for row_idx in range(self.max_rows):

            row_str = []
            for arr in self.layout:
                if row_idx < len(arr):
                    arr_row = [f'{num:>{indent}}' for num in arr[row_idx]]
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

    @property
    def max_rows(self):
        """Maximum number of rows in any seating group."""
        return max(map(len, self.layout))

    def all_passengers_seated(self):
        """Checks if all passengers have been seated."""
        return self.passengers_seated >= self.num_passengers

    def traverse(self):
        """
        A generator to traverse the airplane left to right.

        This generator also makes sure we don't access a row in a seating group where it doesn't exist.
        """
        for row_num in range(self.max_rows):
            for seat_group_num in range(len(self.layout)):
                if row_num >= len(self.layout[seat_group_num]):
                    continue
                yield row_num, seat_group_num

    def assign_aisle_seats(self):
        """Assigns the aisle seats to the passengers."""
        for row_num, seat_group_num in self.traverse():
            seat_group = self.layout[seat_group_num]
            # If not first seat group, put people on the first column
            if seat_group_num != 0:
                self.passengers_seated += 1
                seat_group[row_num][0] = self.passengers_seated
            if self.all_passengers_seated():
                break

            # If not last seat group, put people on the last column
            if seat_group_num != len(self.layout) - 1:
                self.passengers_seated += 1
                seat_group[row_num][-1] = self.passengers_seated
            if self.all_passengers_seated():
                break

    def assign_window_seats(self):
        """Assigns the window seats to the passengers."""
        for row_num, seat_group_num in self.traverse():
            if self.all_passengers_seated():
                break

            seat_group = self.layout[seat_group_num]

            if seat_group_num == 0:
                self.passengers_seated += 1
                seat_group[row_num][0] = self.passengers_seated
                continue

            if seat_group_num == len(self.layout) - 1:
                self.passengers_seated += 1
                seat_group[row_num][-1] = self.passengers_seated
                continue

    def assign_middle_seats(self):
        """Assigns the middle seats to the passengers."""
        for row_num, seat_group_num in self.traverse():
            seat_group = self.layout[seat_group_num]
            cols, _ = self.dims[seat_group_num]
            for col_num in range(1, cols - 1):
                if not self.all_passengers_seated():
                    self.passengers_seated += 1
                    seat_group[row_num][col_num] = self.passengers_seated

    def fill(self):
        """
        Fill the airplane (first aisle, then window and finally middle seats).
        """
        self.assign_aisle_seats()
        self.assign_window_seats()
        self.assign_middle_seats()


def main(input_array, input_passengers):
    """Function to run the program."""
    airplane = Airplane(input_array, input_passengers)
    airplane.fill()
    print(airplane)


if __name__ == "__main__":
    input_array = [[3, 2], [4, 3], [2, 3], [3, 4]]
    input_passengers = 30
    main(input_array, input_passengers)

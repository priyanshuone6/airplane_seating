# ✈️ Airplane Seating Algorithm
It helps seat audiences in a flight by seating passengers starting from the front row to the back, starting from the left to the right, and filling the aisle seats first, followed by window seats, followed by centre seats.

Each number in the output denotes the passenger number. `0` denotes that the seat is empty.

## 📋 Requirements
- Python 3.6 or higher

## 🚀 How to run
To run the program, run the following command in the terminal:
```bash
python main.py
```

## 🚧 How to run tests
This project uses `unittest` for testing. To run the tests, run the following command in the terminal:
```bash
python -m unittest test_main.py
```

## 💻 Example input:
2D array = [[3,2], [4,3], [2,3], [3,4]]

Total passengers = 30

![airplane_seating](https://user-images.githubusercontent.com/64051212/204293617-2bb10240-b031-489c-ac6c-b2ce7c889d62.jpg)

Following the rules, with 30 passengers, the seating output will be:

![airplane_seating_with_num](https://user-images.githubusercontent.com/64051212/204293610-17de9210-3ab5-4338-a3ec-64e0ae19e62e.jpg)

### Test run
```bash
$ python main.py
Airplane Layout
===============
19 25  1     2 26 27  3     4  5     6 28 20
21 29  7     8 30  0  9    10 11    12  0 22
            13  0  0 14    15 16    17  0 23
                                    18  0 24
```
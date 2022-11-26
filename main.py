

class AirplaneSeating:

    def __init__(self, nested_arr, passengers):
        self.nested_arr = nested_arr
        self.passengers = passengers

    def build_layout(self):
        layout = []
        for arr in self.nested_arr:
            cols = arr[0]
            rows = arr[1]

            matrix = []
            for _ in range(rows):
                matrix.append([-1] * cols)
            layout.append(matrix)

        #print(layout[0][0][0])
        #print("\n")

        return layout


    def assign_middle_seats(self, layout):


        for i in range(len(layout)):
            #print(i)
            for j in range(len(layout[i])):
                #print(i,"||||||",j)
                #print(layout[i][j][-1])

                for k in range(1, len(layout[i][j])-1):

                    layout[i][j][k] = "Middle"

                layout[i][j][0] = "Aisle"
                layout[i][j][-1] = "Aisle"

                #print(i,len(layout))

                if i==0:
                    layout[0][j][0] = "Windows"
                if i==len(layout)-1:
                    #print("\n",j,"|||||||||")
                    layout[-1][j][-1] = "Windows"

        return layout



if __name__ == "__main__":
    a = [[3,2], [4,3], [2,3], [3,4]]
    airplane_class = AirplaneSeating(a, 30)
    layout_fun = airplane_class.build_layout()
    middle_seats = airplane_class.assign_middle_seats(layout_fun)

    print(middle_seats)

"""
import numpy

a = [[3,2], [4,3], [2,3], [3,4]]
a = numpy.ndarray(a)


for i in a:
    print(numpy.zeros(i),"\n")



for i in a:
    for j in i:
        print(j, end = " ")
    print()
"""

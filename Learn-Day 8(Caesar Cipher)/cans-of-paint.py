import math


def paint_required(height, width, cover):
    number_of_cans = math.ceil((height*width)/cover)
    print(f"You'll need {number_of_cans} cans of paint")


test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_required(height=test_h, width=test_w, cover=coverage)


# print('%.2f' % a)
# print("{0:.3f}".format(a))

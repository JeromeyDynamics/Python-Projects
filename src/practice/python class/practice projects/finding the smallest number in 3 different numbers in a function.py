def shape1(length, width, height):
    lowest = min(length, width, height)
    return lowest
print(shape1(7,8,9))
print("-----------------------------")
def shape2(length,width,height):
    lowest = float("inf")
    if length<lowest:
        lowest = length
    if width<lowest:
        lowest = width
    if height<lowest:
        lowest = height
    return lowest
print(shape2(7,8,9))
print("-----------------------------")
def shape3(*nums):
    lowest = min(nums)
    return lowest
print(shape3(20,8,13,10,11,9,13,7))
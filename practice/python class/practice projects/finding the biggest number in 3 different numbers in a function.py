def shape(length,width,height):
    highest = max(length, width, height)
    return highest
print(shape(7,8,9))
print("-----------------------------")
def shape(length,width,height):
    highest = 0
    if length>highest:
        highest = length
    if width>highest:
        highest = width
    if height>highest:
        highest = height
    return highest
print(shape(7,8,9))
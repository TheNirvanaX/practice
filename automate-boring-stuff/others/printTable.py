# printTable- this program prints list of list in table format.
def printTable(inp_list):
    col = []
    for list in inp_list:  # determine maximum string len of each col
        collen = [len(i) for i in list]
        col.append(max(collen))

    for y in range(len(inp_list[0])):  # print in table format
        for x in range(len(inp_list)):
            print(inp_list[x][y].rjust(col[x]), end=" ")
        print()


user_list = ableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]
printTable(user_list)

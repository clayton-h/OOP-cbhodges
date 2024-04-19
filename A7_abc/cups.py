#
# Python script that calculates
# the min, max, and range of
# user-provided values
#
# By: Clayton H.
#

# input is either:
# color radius
# or
# diameter color

def sorting(list: list[int | str]) -> list[int | str]:
    for x in list:
        if (x.isdigit()):
            print("int")
        else:
            print("color")

    return list


def main() -> None:
    list = []
    while True:
        line = input()
        if not line.strip():
            break
        input_data = line.split()
        list.append(input_data)
    print(list)
    sorting(list)
    print(list)


if __name__ == "__main__":
    main()

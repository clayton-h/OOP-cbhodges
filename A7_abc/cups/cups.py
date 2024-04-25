#
# Python script that calculates
# the min, max, and range of
# user-provided values
#
# By: Clayton H.
#


from backend import Backend


def main() -> None:
    backend = Backend()
    backend.read_input()
    backend.solve()
    backend.print_answer()


if __name__ == "__main__":
    main()

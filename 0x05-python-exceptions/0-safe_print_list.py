#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    lenght = 0
    try:
        for ele in my_list:
            if (lenght >= x):
                break
            print("{}".format(ele), end="")
            lenght += 1
        return lenght
    except IndexError:
        pass
    finally:
        print()

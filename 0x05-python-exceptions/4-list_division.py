#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    div_result = 0
    for ele in range(list_length):
        try:
            div_result = my_list_1[ele] / my_list_2[ele]
        except TypeError:
            print("wrong type")
            div_result = 0
        except ZeroDivisionError:
            print("division by 0")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            div_list.append(div_result)
    return div_list

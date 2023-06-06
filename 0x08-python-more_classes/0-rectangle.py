#!/usr/bin/python3

class Rectangle:
    pass

if __name__ == "__main__":
    my_rectangle = Rectangle()
    class_name = type(my_rectangle).__name__
    file_name = __file__.split("/")[-1].split(".")[0]
    print(f"<class '{file_name}.{class_name}'>")
    print("{}")



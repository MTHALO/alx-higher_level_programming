[2;2R[>77;30601;0c]10;rgb:f8f8/f8f8/f2f2]11;rgb:2828/2a2a/3636#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

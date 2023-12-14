from typing import Optional, Type, Union


class Singleton:
    _instance: Optional["Singleton"] = None

    def __new__(cls) -> "Union[Type[Singleton], Singleton]":
        if not cls._instance:
            print("Create Singleton")
            cls._instance = super().__new__(cls)
            cls._instance.__init__()
        print("Return Singleton")
        return cls._instance

    def __init__(self):
        print("Init Singleton")

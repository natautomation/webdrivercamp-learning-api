import json

def from_json_file(file_name: str):
    """
    Deserialize JSON data from a file and return the corresponding Python object.

    Parameters:
    - file_name (str): The name of the file containing JSON data.

    Returns:
    - dict: The Python object representing the deserialized JSON data.
    """
    with open(file_name, "r", encoding='utf-8') as file:
        return json.load(file)


if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.json"

    data_object = from_json_file(file_name)

    print(data_object)
    print(type(data_object))
    print()
    for key, val in data_object.items():
        print(f"{key}: {type(val).__name__}")

#output
# {'list': [1, 2, 3, 4, 5], 'tuple': [1, 2, 3, 4, 5], 'string': 'Hello World!', 'bool': False, 'null': None, 'int': 123, 'float': 3.14, 'dict': {'abc': True, 'Hello': 'World', '10': [2, 3, 4]}}
# <class 'dict'>
#
# list: list
# tuple: list
# string: str
# bool: bool
# null: NoneType
# int: int
# float: float
# dict: dict
#
# Process finished with exit code 0

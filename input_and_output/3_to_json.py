"""To JSON exercise"""
import json

def to_json(data):
    """Serializing data"""

    return json.dumps(data)
    # adding code

if __name__ == "__main__":
    data_types = [[1, 2, 3, 4, 5],
                  (1, 2, 3, 4, 5),
                  "Hello World!",
                  False,
                  None,
                  123,
                  3.14,
                  {"abc": True, "Hello": "World", 10: [2, 3, 4]},
                  {"a", "b", "c"}]
    try:
        for data in data_types:
            json_data = to_json(data)
            print(f"{f'{data}:':17} {type(data).__name__:10} => {json_data}: {type(json_data).__name__}")
    except Exception as e:
        print("ERROR:")
        print(f"\t{data}: {type(data).__name__} => {e}")

#output
# [1, 2, 3, 4, 5]:  list       => [1, 2, 3, 4, 5]: str
# (1, 2, 3, 4, 5):  tuple      => [1, 2, 3, 4, 5]: str
# Hello World!:     str        => "Hello World!": str
# False:            bool       => false: str
# None:             NoneType   => null: str
# 123:              int        => 123: str
# 3.14:             float      => 3.14: str
# {'abc': True, 'Hello': 'World', 10: [2, 3, 4]}: dict       => {"abc": true, "Hello": "World", "10": [2, 3, 4]}: str
# ERROR:
# 	{'a', 'b', 'c'}: set => Object of type set is not JSON serializable
#
# Process finished with exit code 0

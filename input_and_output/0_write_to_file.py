"""
Writing data into a file.
"""

def write_to_file(data: str, filename: str) -> int:
    """
    Write the provided data to  the specified file.

    Parameters:
    - data (str): The data to be written to the file.
    - filename (str): The name of the file where data will be written to.

    Returns:
    - int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as writer:
        writer.write(data)
        return len(data)

if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    data = """
    In the beginning the Universe was created. 
    This has made a lot of people very angry and been widely regarded as a bad move."""

    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")
    print()
    print(f"Number of char: {write_to_file(data, file_name)}")
    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")
    print()
    data = "Don't Panic"
    print(f"Number of char: {write_to_file(data, file_name)}")
    print(f"Files: {next(os.walk(dir_path), (None, None, []))[2]}")
    
#output
# Files: ['3_to_json.py', '1_append_to_file_0.py', '5_from_json_file.py', '4_json_to_file_0.py',
    #         '0_write_to_file_0.py', '1_append_to_file.py', '2_read_a_file_0.py', 'data.json', 'README.md',
    #         '3_to_json_0.py', '5_from_json_file_0.py', '0_write_to_file.py', '4_json_to_file.py',
    #         'my_info_token_natautomation.txt', 'data.txt', '2_read_a_file.py']
    #
    # Number
    # of
    # char: 133
    # Files: ['3_to_json.py', '1_append_to_file_0.py', '5_from_json_file.py', '4_json_to_file_0.py',
    #         '0_write_to_file_0.py', '1_append_to_file.py', '2_read_a_file_0.py', 'data.json', 'README.md',
    #         '3_to_json_0.py', '5_from_json_file_0.py', '0_write_to_file.py', '4_json_to_file.py',
    #         'my_info_token_natautomation.txt', 'data.txt', '2_read_a_file.py']
    #
    # Number
    # of
    # char: 11
    # Files: ['3_to_json.py', '1_append_to_file_0.py', '5_from_json_file.py', '4_json_to_file_0.py',
    #         '0_write_to_file_0.py', '1_append_to_file.py', '2_read_a_file_0.py', 'data.json', 'README.md',
    #         '3_to_json_0.py', '5_from_json_file_0.py', '0_write_to_file.py', '4_json_to_file.py',
    #         'my_info_token_natautomation.txt', 'data.txt', '2_read_a_file.py']
    #
    # Process
    # finished
    # with exit code 0

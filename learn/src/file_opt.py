"""
File Operations Programming Assignment
"""


def read_file(file_name: str) -> str:
    """Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE
    with open(file_name, encoding="utf-8") as file:
        content = file.read()
        print(content)
        return content


def read_file_into_list(file_name: str) -> list[str]:
    """Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE
    with open(file_name, encoding="utf-8") as file:
        content_list = file.readlines()
        return content_list


def write_first_line_to_file(file_contents: str, output_filename: str) -> None:
    """Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
    with open(output_filename, mode="w", encoding="utf-8") as output:
        output.write(file_contents.split(sep="\n")[0])


def read_even_numbered_lines(file_name: str) -> list[str]:
    """Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE
    with open(file_name, encoding="utf-8") as file:
        content = file.readlines()
        even_list: list[str] = []
        for even_index in range(1, len(content), 2):
            even_list.append(content[even_index])
        return even_list


def read_file_in_reverse(file_name: str) -> list[str]:
    """Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    with open(file_name, encoding="utf-8") as file:
        content = file.readlines()
        content_itr = reversed(content)
        reversed_content = []
        for line in content_itr:
            reversed_content.append(line)
        return reversed_content


def main() -> None:
    "main"
    read_file("learning/sampletext.txt")
    print(read_file_into_list("learning/sampletext.txt"))
    write_first_line_to_file(
        read_file("learning/sampletext.txt"), "learning/oneline.txt",
    )
    print(read_even_numbered_lines("learning/sampletext.txt"))
    print(read_file_in_reverse("learning/sampletext.txt"))


if __name__ == "__main__":
    main()

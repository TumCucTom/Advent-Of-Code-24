def read_lists_from_file(file_path):
    """
    Reads two vertical lists from a file and stores them in two arrays.

    Args:
        file_path (str): The path to the file containing two columns of numbers.

    Returns:
        tuple: Two lists of numbers.
    """
    list1, list2 = [], []

    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into two numbers
            num1, num2 = map(float, line.split())
            list1.append(num1)
            list2.append(num2)

    return list1, list2

def calculate_weighted_sum(file_path):
    """
    Reads two lists from a file, counts occurrences of each number in the second list, 
    and computes the weighted sum of the numbers in the first list.

    Args:
        file_path (str): The path to the file containing two columns of numbers.

    Returns:
        float: The weighted sum of numbers in the first list.
    """
    # Read the lists from the file
    list1, list2 = read_lists_from_file(file_path)

    # Count occurrences of each number in the second list
    counts = {num: list2.count(num) for num in set(list2)}

    # Calculate the weighted sum
    weighted_sum = sum(num * counts.get(num, 0) for num in list1)

    return weighted_sum

# Example usage
file_path = "Data/1.txt"  # Replace with the path to your file
result = calculate_weighted_sum(file_path)
print(f"Weighted sum: {result}")

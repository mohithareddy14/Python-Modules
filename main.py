"""Main script that demonstrates all ten standard-library modules."""

from datetime_util import get_current_datetime
from json_util import convert_to_json
from random_util import generate_random_number
from os_util import get_current_directory
from re_util import find_numbers
from collections_util import count_items
from itertools_util import combine_lists
from math_util import calculate_square_root
from statistics_util import calculate_average
from pathlib_util import check_file_exists


print("1. Current Date and Time:")
print(get_current_datetime())

print("\n2. JSON Conversion:")
print(convert_to_json())

print("\n3. Random Number:")
print(generate_random_number())

print("\n4. Current Directory:")
print(get_current_directory())

print("\n5. Numbers Found Using Regex:")
print(find_numbers())

print("\n6. Item Frequency:")
print(count_items())

print("\n7. Combined List:")
print(combine_lists())

print("\n8. Square Root:")
print(calculate_square_root())

print("\n9. Average:")
print(calculate_average())

print("\n10. File Exists:")
print(check_file_exists())
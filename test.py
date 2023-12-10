exam_format = [
    ("Test 1", "Multiple Choice", 10),
    ("Test 2", "Identification", 10),
    ("Test 3", "True or False", 10),
    ("Test 4", "Fill in the Blanks", 10),
    ("Test 5","Essay", 10)
]

exam_format_str = '\n'.join(str(t) for t in exam_format)

print(exam_format_str)
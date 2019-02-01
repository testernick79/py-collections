COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(sets):
    lists = []
    for key, value in COURSES.items():
        if value & sets:
            lists.append(key)
            print(lists)

    return lists

covers({'Ruby'})

def covers_all(arguments):
    outputs = []
    for key, value in COURSES.items():
        if value.intersection(arguments) == arguments:
            outputs.append(key)

    return outputs



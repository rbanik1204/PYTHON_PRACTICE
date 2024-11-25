# nesting of dictionaries

student_data = [{
    "Name": "Ram",
    "Roll": 67,
    "Course": {"C", "Python"}
}, {"Name": "Jenny",
    "Roll": 1,
    "Course": {"C", "C++", "Java"}
    }
]


def add_dict(Name, Roll, Course):
    new_sub_dict = dict()
    new_sub_dict["Name"] = Name
    new_sub_dict["Roll"] = Roll
    new_sub_dict["Course"] = Course
    student_data.append(new_sub_dict)


add_dict(Name="Ritu", Roll=69, Course={"C", "java"})
print(student_data)

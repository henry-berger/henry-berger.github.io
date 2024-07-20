import json

with open("courses.json", "r") as f:
    courses = json.load(f)
    print(courses)

def course_format(course):
    # return f"- **{course['name']}** ({course['code']}) with {course['prof']}, _{course['sem']} {course['year']}_\n"
    return f"- {course['name']} ({course['code']}) _with Prof. {course['prof']}_\n"

with open("coursework.md", "w") as f:
    f.write("""---
layout: archive
title: "Relevant Coursework"
permalink: /coursework/
author_profile: true
---

{% include base_path %}

Below is a selection of robotics-related classes I have taken at Yale:
""")


    f.write("\n### Robotics\n")
    for course in courses["Robotics"]:
        f.write(course_format(course))

    f.write("\n### Computer Science Fundamentals\n")
    for course in courses["Computer Science"]:
        f.write(course_format(course))

    f.write("\n### Math Fundamentals\n")
    for course in courses["Mathematics"]:
        f.write(course_format(course))

    f.write("\n### Mechanical Engineering Fundamentals\n")
    for course in courses["Mechanical Engineering"]:
        f.write(course_format(course))

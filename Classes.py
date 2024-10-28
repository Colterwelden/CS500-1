course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}


def display_course_info(course_number):
    if course_number in course_rooms:
        # Retrieve course details from dictionaries
        room = course_rooms[course_number]
        instructor = course_instructors[course_number]
        time = course_times[course_number]
        
        print(f"Course Number: {course_number}")
        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {time}")
    else:
        # If the course number is not found
        print("Course not found. Please enter a valid course number.")

def main():
    while True:
        course_number = input("Available courses: CSC101, CSC102, CSC103, NET110, COM241. Enter a course number (or 'q' to quit): ")
        if course_number.lower() == 'q':
            print("Exiting the program.")
            break
        else:
            display_course_info(course_number)


if __name__ == "__main__":
    main()

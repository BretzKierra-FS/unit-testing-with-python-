test_cases = [
    # A grade
    (("John", "Homework", "95"), "Hello John\nYour letter grade for Homework assignment is as follows: A\nAssignment details:\nYou have met most or all of the assignment's requirements."),
    # B grade
    (("John", "Homework", "85"), "Hello John\nYour letter grade for Homework assignment is as follows: B\nAssignment details:\nYou have met most of the assignment's requirements."),
    # C grade
    (("John", "Homework", "75"), "Hello John\nYour letter grade for Homework assignment is as follows: C\nAssignment details:\nYou have met many of the assignment's requirements."),
    # D grade
    (("John", "Homework", "65"), "Hello John\nYour letter grade for Homework assignment is as follows: D\nAssignment details:\nYou have met some of the assignment's requirements."),
    # F grade
    (("John", "Homework", "55"), 55),
]
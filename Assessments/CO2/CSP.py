subjects = ['AI', 'OS', 'DBMS', 'CN']

domains = {
    'AI': ['Monday', 'Tuesday'],
    'OS': ['Monday', 'Tuesday'],
    'DBMS': ['Tuesday', 'Wednesday'],
    'CN': ['Monday', 'Wednesday']
}

assignment = {}

def is_valid(subject, day):
    for other in assignment:
        if assignment[other] == day:
            return False
    return True

def solve():
    if len(assignment) == len(subjects):
        return True

    # MRV: choose subject with smallest remaining domain
    unassigned = [s for s in subjects if s not in assignment]
    subject = min(unassigned, key=lambda s: len(domains[s]))

    for day in domains[subject]:
        if is_valid(subject, day):
            assignment[subject] = day

            if solve():
                return True

            del assignment[subject]

    return False

if solve():
    print("Exam Timetable:")
    for subject, day in assignment.items():
        print(subject, "->", day)
else:
    print("No solution")
# Experiment 24: Backward Chaining
# Goal-Driven Reasoning

facts = {
    "fever",
    "cough"
}

rules = {
    "flu": {"fever", "cough"},
    "rest": {"flu"},
    "doctor_visit": {"flu", "rest"}
}


def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()

    if goal in facts:
        return True

    if goal in visited:
        return False

    visited.add(goal)

    if goal not in rules:
        return False

    conditions = rules[goal]

    for condition in conditions:
        if not backward_chaining(condition, facts, rules, visited):
            return False

    return True


print("BACKWARD CHAINING")
print("------------------")

goal = input("Enter goal: ").lower()

if backward_chaining(goal, facts, rules):
    print("Goal", goal, "can be proved from the given facts.")
else:
    print("Goal", goal, "cannot be proved from the given facts.")
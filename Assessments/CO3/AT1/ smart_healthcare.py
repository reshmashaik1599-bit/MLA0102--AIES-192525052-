# smart_healthcare.py
# Smart Healthcare Diagnosis System
# Artificial Intelligence and Expert Systems - CO3

# ---------------------------------------------------------
# 1. KNOWLEDGE BASE
# ---------------------------------------------------------

# Facts about Ravi
facts = {
    ("Fever", "Ravi"),
    ("Cough", "Ravi"),
    ("BodyPain", "Ravi")
}

# Rules:
# Fever(x) AND Cough(x) -> Flu(x)
# Flu(x) AND BodyPain(x) -> ViralInfection(x)
# ViralInfection(x) -> NeedsRest(x)

rules = [
    {
        "conditions": [("Fever", "x"), ("Cough", "x")],
        "conclusion": ("Flu", "x")
    },
    {
        "conditions": [("Flu", "x"), ("BodyPain", "x")],
        "conclusion": ("ViralInfection", "x")
    },
    {
        "conditions": [("ViralInfection", "x")],
        "conclusion": ("NeedsRest", "x")
    }
]


# ---------------------------------------------------------
# 2. UNIFICATION
# ---------------------------------------------------------

def unify(pattern, fact):
    """
    Unifies a predicate pattern with a known fact.

    Example:
    pattern = ("Fever", "x")
    fact    = ("Fever", "Ravi")

    Result:
    {'x': 'Ravi'}
    """

    if pattern[0] != fact[0]:
        return None

    substitution = {}

    for p, f in zip(pattern, fact):
        if p == "x":
            substitution["x"] = f
        elif p != f:
            return None

    return substitution


# ---------------------------------------------------------
# 3. APPLY SUBSTITUTION
# ---------------------------------------------------------

def apply_substitution(predicate, substitution):
    """
    Replaces variables with their values.
    """

    return tuple(
        substitution.get(item, item)
        for item in predicate
    )


# ---------------------------------------------------------
# 4. FORWARD CHAINING
# ---------------------------------------------------------

def forward_chaining(initial_facts, rules):
    """
    Forward chaining starts with known facts and applies
    rules to derive new facts.
    """

    known_facts = set(initial_facts)

    changed = True

    while changed:
        changed = False

        for rule in rules:

            # Find the person/entity from the first condition
            first_condition = rule["conditions"][0]

            for fact in list(known_facts):

                substitution = unify(first_condition, fact)

                if substitution is None:
                    continue

                # Check whether all conditions are satisfied
                all_conditions_true = True

                for condition in rule["conditions"]:

                    required = apply_substitution(
                        condition,
                        substitution
                    )

                    if required not in known_facts:
                        all_conditions_true = False
                        break

                # If all conditions are true, derive conclusion
                if all_conditions_true:

                    conclusion = apply_substitution(
                        rule["conclusion"],
                        substitution
                    )

                    if conclusion not in known_facts:
                        known_facts.add(conclusion)

                        print(
                            "New fact derived:",
                            conclusion
                        )

                        changed = True

    return known_facts


# ---------------------------------------------------------
# 5. BACKWARD CHAINING
# ---------------------------------------------------------

def backward_chaining(goal, facts, rules, visited=None):
    """
    Backward chaining starts with a goal and works backward
    to determine whether the goal can be proved.
    """

    if visited is None:
        visited = set()

    # Goal is already a known fact
    if goal in facts:
        return True

    if goal in visited:
        return False

    visited.add(goal)

    # Search for a rule that produces the goal
    for rule in rules:

        conclusion = rule["conclusion"]

        # Check predicate name
        if conclusion[0] != goal[0]:
            continue

        # Create substitution
        substitution = {}

        if conclusion[1] == "x":
            substitution["x"] = goal[1]

        # Check every condition
        conditions_proved = True

        for condition in rule["conditions"]:

            required = apply_substitution(
                condition,
                substitution
            )

            if not backward_chaining(
                required,
                facts,
                rules,
                visited
            ):
                conditions_proved = False
                break

        if conditions_proved:
            return True

    return False


# ---------------------------------------------------------
# 6. DISPLAY KNOWLEDGE BASE
# ---------------------------------------------------------

def display_knowledge_base():
    print("\n========== KNOWLEDGE BASE ==========")

    print("\nFacts:")

    for fact in facts:
        print(" ", fact)

    print("\nRules:")

    print(" Fever(x) AND Cough(x) -> Flu(x)")
    print(" Flu(x) AND BodyPain(x) -> ViralInfection(x)")
    print(" ViralInfection(x) -> NeedsRest(x)")


# ---------------------------------------------------------
# 7. MAIN PROGRAM
# ---------------------------------------------------------

def main():

    print("==============================================")
    print("   SMART HEALTHCARE DIAGNOSIS SYSTEM")
    print("==============================================")

    display_knowledge_base()

    # -----------------------------------------------------
    # Unification demonstration
    # -----------------------------------------------------

    print("\n========== UNIFICATION ==========")

    pattern1 = ("Fever", "x")
    fact1 = ("Fever", "Ravi")

    result1 = unify(pattern1, fact1)

    print("\nExample 1:")
    print("Pattern :", pattern1)
    print("Fact    :", fact1)
    print("Result  :", result1)

    pattern2 = ("Cough", "x")
    fact2 = ("Cough", "Ravi")

    result2 = unify(pattern2, fact2)

    print("\nExample 2:")
    print("Pattern :", pattern2)
    print("Fact    :", fact2)
    print("Result  :", result2)

    # -----------------------------------------------------
    # Forward Chaining
    # -----------------------------------------------------

    print("\n========== FORWARD CHAINING ==========")

    derived_facts = forward_chaining(facts, rules)

    print("\nAll derived facts:")

    for fact in sorted(derived_facts):
        print(" ", fact)

    # -----------------------------------------------------
    # Backward Chaining
    # -----------------------------------------------------

    print("\n========== BACKWARD CHAINING ==========")

    query = ("NeedsRest", "Ravi")

    print("\nQuery:", query)

    result = backward_chaining(
        query,
        derived_facts,
        rules
    )

    if result:
        print("Result: PROVED")
        print("Ravi needs rest.")
    else:
        print("Result: NOT PROVED")

    # -----------------------------------------------------
    # Final Diagnosis
    # -----------------------------------------------------

    print("\n========== FINAL INFERENCE ==========")

    if ("Flu", "Ravi") in derived_facts:
        print("Ravi may have FLU.")

    if ("ViralInfection", "Ravi") in derived_facts:
        print("Ravi may have a VIRAL INFECTION.")

    if ("NeedsRest", "Ravi") in derived_facts:
        print("Advice: Ravi should REST.")

    print("\n==============================================")
    print("        INFERENCE COMPLETED")
    print("==============================================")


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
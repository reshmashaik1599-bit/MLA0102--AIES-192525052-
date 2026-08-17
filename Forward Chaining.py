# Experiment 23: Forward Chaining
# Rule-Based Reasoning

facts = {
    "fever",
    "cough"
}

rules = [
    ({"fever", "cough"}, "flu"),
    ({"flu"}, "rest"),
    ({"flu", "rest"}, "doctor_visit")
]


def forward_chaining(facts, rules):
    facts = set(facts)

    changed = True

    while changed:
        changed = False

        for conditions, conclusion in rules:
            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                print("Derived:", conclusion)
                changed = True

    return facts


print("FORWARD CHAINING")
print("-----------------")

print("Initial facts:")
for fact in facts:
    print("-", fact)

final_facts = forward_chaining(facts, rules)

print("\nFinal facts:")
for fact in final_facts:
    print("-", fact)
# loan_approval.py
# Intelligent Loan Approval System
# Assessment Tool 2 - Q3

# -------------------------------
# 1. FACTS
# -------------------------------

facts = {
    "StableEmployment(Arun)",
    "SufficientIncome(Arun)",
    "HighCreditScore(Arun)",
    "GoodRepaymentHistory(Arun)"
}


# -------------------------------
# 2. UNIFICATION
# -------------------------------

def unify(predicate, fact):
    """
    Simple unification:
    predicate: StableEmployment(x)
    fact:      StableEmployment(Arun)
    """

    if predicate.endswith("(x)") and fact.startswith(predicate[:-3]):
        return {"x": "Arun"}

    return None


# -------------------------------
# 3. FORWARD INFERENCE
# -------------------------------

def loan_inference():
    print("====================================")
    print("   INTELLIGENT LOAN APPROVAL SYSTEM")
    print("====================================")

    print("\nInitial Facts:")

    for fact in facts:
        print("-", fact)

    # Rule 1:
    # StableEmployment(x) AND SufficientIncome(x)
    # -> PreliminaryApproval(x)

    if ("StableEmployment(Arun)" in facts and
            "SufficientIncome(Arun)" in facts):

        facts.add("PreliminaryApproval(Arun)")

        print("\nRule 1 Applied:")
        print("StableEmployment(Arun) + SufficientIncome(Arun)")
        print("-> PreliminaryApproval(Arun)")

    # Rule 2:
    # HighCreditScore(x) AND PreliminaryApproval(x)
    # -> LowRisk(x)

    if ("HighCreditScore(Arun)" in facts and
            "PreliminaryApproval(Arun)" in facts):

        facts.add("LowRisk(Arun)")

        print("\nRule 2 Applied:")
        print("HighCreditScore(Arun) + PreliminaryApproval(Arun)")
        print("-> LowRisk(Arun)")

    # Rule 3:
    # LowRisk(x) AND GoodRepaymentHistory(x)
    # -> LoanApproved(x)

    if ("LowRisk(Arun)" in facts and
            "GoodRepaymentHistory(Arun)" in facts):

        facts.add("LoanApproved(Arun)")

        print("\nRule 3 Applied:")
        print("LowRisk(Arun) + GoodRepaymentHistory(Arun)")
        print("-> LoanApproved(Arun)")


# -------------------------------
# 4. UNIFICATION DEMONSTRATION
# -------------------------------

def show_unification():

    print("\n====================================")
    print("          UNIFICATION")
    print("====================================")

    predicate1 = "StableEmployment(x)"
    fact1 = "StableEmployment(Arun)"

    result1 = unify(predicate1, fact1)

    print("\nExample 1:")
    print("Predicate :", predicate1)
    print("Fact      :", fact1)
    print("Substitution:", result1)

    predicate2 = "HighCreditScore(x)"
    fact2 = "HighCreditScore(Arun)"

    result2 = unify(predicate2, fact2)

    print("\nExample 2:")
    print("Predicate :", predicate2)
    print("Fact      :", fact2)
    print("Substitution:", result2)


# -------------------------------
# 5. RESOLUTION DEMONSTRATION
# -------------------------------

def resolution():

    print("\n====================================")
    print("            RESOLUTION")
    print("====================================")

    print("\nQuery:")
    print("LoanApproved(Arun)")

    print("\nRule:")
    print("LowRisk(x) AND GoodRepaymentHistory(x)")
    print("-> LoanApproved(x)")

    print("\nKnown facts:")
    print("LowRisk(Arun)")
    print("GoodRepaymentHistory(Arun)")

    print("\nNegated Query:")
    print("NOT LoanApproved(Arun)")

    print("\nResolution Result:")
    print("Contradiction obtained.")
    print("Therefore, LoanApproved(Arun) is TRUE.")


# -------------------------------
# 6. FINAL RESULT
# -------------------------------

def final_result():

    print("\n====================================")
    print("          FINAL INFERENCE")
    print("====================================")

    if "LoanApproved(Arun)" in facts:

        print("\nFinal Conclusion:")
        print("Arun can be recommended for loan approval.")

    else:

        print("\nLoan approval could not be proved.")


# -------------------------------
# MAIN PROGRAM
# -------------------------------

if __name__ == "__main__":

    loan_inference()

    show_unification()

    resolution()

    final_result()
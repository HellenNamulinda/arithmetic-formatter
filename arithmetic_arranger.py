def arithmetic_arranger(problems, answer=False):
    # Check the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operand = []
    second_operand = []
    operators = []

    for problem in problems:
        strings = problem.split()
        first_operand.append(strings[0])
        operators.append(strings[1])
        second_operand.append(strings[2])

    # Check for * or /
    if "*" in operators or "/" in operators:
        return "Error: Operator must be '+' or '-'."

    # Check the digits
    for i in range(len(first_operand)):
        if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check the length
    for i in range(len(first_operand)):
        if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    first_row = []
    second_row = []
    third_row = []
    fourth_row = []

    for i in range(len(first_operand)):
        if len(first_operand[i]) > len(second_operand[i]):
            first_row.append(" "*2 + first_operand[i])
        else:
            first_row.append(
                " "*(len(second_operand[i]) - len(first_operand[i]) + 2) + first_operand[i])

    for i in range(len(second_operand)):
        if len(second_operand[i]) > len(first_operand[i]):
            second_row.append(operators[i] + " " + second_operand[i])
        else:
            second_row.append(
                operators[i] + " "*(len(first_operand[i]) - len(second_operand[i]) + 1) + second_operand[i])

    for i in range(len(first_operand)):
        third_row.append(
            "-"*(max(len(first_operand[i]), len(second_operand[i])) + 2))

    if answer:
        for i in range(len(first_operand)):
            if operators[i] == "+":
                ans = str(int(first_operand[i]) + int(second_operand[i]))
            else:
                ans = str(int(first_operand[i]) - int(second_operand[i]))

            if len(ans) > max(len(first_operand[i]), len(second_operand[i])):
                fourth_row.append(" " + ans)
            else:
                fourth_row.append(
                    " "*(max(len(first_operand[i]), len(second_operand[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(first_row) + "\n" + "    ".join(
            second_row) + "\n" + "    ".join(third_row) + "\n" + "    ".join(fourth_row)
    else:
        arranged_problems = "    ".join(
            first_row) + "\n" + "    ".join(second_row) + "\n" + "    ".join(third_row)
    return arranged_problems
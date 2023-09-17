def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    top_lines = []
    operator_lines = []
    bottom_lines = []
    result_lines = []

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_width = max(len(num1), len(num2))

        top_line = f"{num1:>{max_width+2}}"
        operator_line = f"{operator} {num2:>{max_width}}"
        bottom_line = "-" * (max_width + 2)

        if operator == "+":
            result = str(int(num1) + int(num2))
        else:
            result = str(int(num1) - int(num2))

        result_line = f"{result:>{max_width+2}}"

        top_lines.append(top_line)
        operator_lines.append(operator_line)
        bottom_lines.append(bottom_line)
        result_lines.append(result_line)

    top = "    ".join(top_lines)
    operator = "    ".join(operator_lines)
    bottom = "    ".join(bottom_lines)
    result = "    ".join(result_lines)

    arranged_problem = f"{top}\n{operator}\n{bottom}"
    if show_answers:
        arranged_problem += f"\n{result}"

    return arranged_problem

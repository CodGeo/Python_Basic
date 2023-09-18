class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23} {item['amount']:.2f}\n"
            total += item["amount"]
        return title + items + f"Total: {total:.2f}"

    def get_withdrawals(self):
        return sum(item["amount"] for item in self.ledger if item["amount"] < 0)


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    # Calculate spending percentages
    total_spent = sum(category.get_withdrawals() for category in categories)
    percentages = [(category.get_withdrawals() / total_spent) * 100 for category in categories]

    # Create the chart lines for each percentage
    lines = []
    for i in range(100, -1, -10):
        line = str(i).rjust(3) + "| "
        for percentage in percentages:
            line += "o  " if percentage >= i else "   "
        lines.append(line)

    # Add the horizontal line
    dash_line = "    -" + "---" * len(categories)
    lines.append(dash_line)

    # Determine the maximum category name length
    max_name_length = max(len(category.category) for category in categories)

    # Create lines for category names
    for i in range(max_name_length):
        name_line = "     "
        for category in categories:
            if i < len(category.category):
                name_line += category.category[i] + "  "
            else:
                name_line += "   "
        lines.append(name_line)

    # Adjust spacing based on the presence of 'o' in each line
    max_line_length = max(len(line) for line in lines)
    for i in range(len(lines)):
        lines[i] = lines[i].ljust(max_line_length)

    # Combine lines into the final chart
    chart += "\n".join(lines)

    return chart

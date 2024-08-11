from colorama import Fore, Back, Style
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name  # Private attribute for category name
        self.__allocated_budget = allocated_budget  # Private attribute for allocated budget

    # Method to get the category name
    def get_category_name(self):
        return self.__category_name         

    # Method to get the allocated budget          # Getters
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Method to set a new allocated budget with validation
    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self.__allocated_budget = new_budget        # Setter
        else:
            raise ValueError("Budget must be a positive number! :P")

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name 
        self.__allocated_budget = allocated_budget
        self.__expenses = 0  # Initialize expenses to 0

    def get_category_name(self):
        return self.__category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self.__allocated_budget = new_budget
        else:
            raise ValueError("Budget must be a positive number! V_V")

    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__allocated_budget - self.__expenses:
                self.__expenses += amount
            else:
                raise ValueError("Expense exceeds the remaining budget! :()")
        else:
            raise ValueError("Expense amount must be positive! >.<")

    def get_remaining_budget(self):
        return self.__allocated_budget - self.__expenses

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = 0

    def get_category_name(self):
        return self.__category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
           self.__allocated_budget == new_budget 
        else:
            raise ValueError("Budget must be a positive number! :/")

    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__allocated_budget - self.__expenses:
                self.__expenses += amount
            else:
                raise ValueError("Expense exceeds the remaining budget :P")
        else:
            raise ValueError("Expense amount must be positive! >:D")

    def get_remaining_budget(self):
        return self.__allocated_budget - self.__expenses

    def display_details(self):
        print(f"Category: {Fore.CYAN + self.__category_name + Style.RESET_ALL}")
        print(Fore.YELLOW + f"Allocated Budget: ${self.__allocated_budget}" + Style.RESET_ALL)
        print(Fore.RED + f"Expenses: ${self.__expenses}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Remaining Budget: ${self.get_remaining_budget()}" + Style.RESET_ALL)
        print("---" * 10)

# Create an instance of BudgetCategory
food_budget = BudgetCategory("Food", 500)
entertainment_budget = BudgetCategory("entertainment",700)
balloon_budget = BudgetCategory("balloon", 50)
alcohol_budget = BudgetCategory("alcohol", 205)
# Add expenses
food_budget.add_expense(50)
food_budget.add_expense(100)
entertainment_budget.add_expense(500)
balloon_budget.add_expense(40)
alcohol_budget.add_expense(175)
alcohol_budget.add_expense(25)
# Display budget details
food_budget.display_details()
entertainment_budget.display_details()
balloon_budget.display_details()
alcohol_budget.display_details()


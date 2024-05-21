class TaxCalculator:
    TAX_BRACKETS = {
        (0, 300000): 0.0,
        (300001, 400000): 0.1,
        (400001, 650000): 0.15,
        (650001, 1000000): 0.2,
        (1000001, 1500000): 0.25,
        (1500001, float('inf')): 0.3
    }

    staticmethod
    def calculate_tax(taxable_income):
        total_tax = 0
        for lower_bound, upper_bound in TaxCalculator.TAX_BRACKETS:
            if lower_bound <= taxable_income <= upper_bound:
                tax_rate = TaxCalculator.TAX_BRACKETS[(lower_bound, upper_bound)]
                total_tax += tax_rate * (taxable_income - lower_bound + 1)
        if total_tax >= 1000000:
            total_tax *= 1.1
        return total_tax


class Employee:
    def __init__(self, name, age, salary, deductions, bonus=0, num_children=0, child_education_allowance=0):
        self.name = name
        self.age = age
        self.salary = salary
        self.deductions = deductions
        self.bonus = bonus
        self.num_children = num_children
        self.child_education_allowance = child_education_allowance

    def calculate_taxable_income(self):
        taxable_income = self.salary + self.bonus - self.deductions - self.child_education_allowance * self.num_children
        return max(0, taxable_income)

    def calculate_personal_income_tax(self):
        if self.age < 18:
            return "Not liable to pay tax as you are under age."

        taxable_income = self.calculate_taxable_income()

        if taxable_income == 0:
            return "No tax payable as taxable income is zero."

        return TaxCalculator.calculate_tax(taxable_income)


# Example usage
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your annual salary: "))
deductions = float(input("Enter your total deductions: "))
bonus = float(input("Enter your annual bonus (if any): "))
num_children = int(input("Enter the number of children: "))
child_education_allowance = float(input("Enter the child education allowance per child: "))

employee = Employee(name, age, salary, deductions, bonus, num_children, child_education_allowance)
tax_payable = employee.calculate_personal_income_tax()
print(f"Tax payable by {employee.name}")
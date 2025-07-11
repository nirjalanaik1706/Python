class Management:
    def communicate(self, message):
        return f"Management Communication: {message}"

class HR(Management):
    def employee_details(self, name, id):
        return f"Employee Name: {name}, ID: {id}"

class Accounts(Management):
    def salary_details(self, name, amount, leaves):
        deducted_amount = amount - (leaves * 500)
        return f"Salary of {name} after deducting {leaves} leaves is {deducted_amount}"

class Advertisements(Management):
    def campaign(self, product, budget):
        return f"Advertising {product} with a budget of {budget}"

hr = HR()
accounts = Accounts()
ads = Advertisements()
management = Management()

print(management.communicate("All departments should follow the new policy."))
print(hr.employee_details("NIRJALA", 101))
print(accounts.salary_details("NIRJALA", 50000, 2))
print(ads.campaign("New Phone", 100000))
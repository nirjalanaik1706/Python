class HR:
    def employee_details(self, name, id):
        return f"Employee Name: {name}, ID: {id}"

class Accounts:
    def salary_details(self, name, amount):
        return f"Salary of {name} is {amount}"

class Advertisements:
    def campaign(self, product, budget):
        return f"Advertising {product} with a budget of {budget}"

class Management:
    def project_details(self, project, deadline):
        return f"Project: {project}, Deadline: {deadline}"

hr = HR()
accounts = Accounts()
ads = Advertisements()
management = Management()

print(hr.employee_details("Nirjala", 101))
print(accounts.salary_details("Nirjala", 50000))
print(ads.campaign("New Phone", 100000))
print(management.project_details("Website Design", "31 Dec"))

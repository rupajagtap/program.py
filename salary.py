class Employee:
    def AcceptEmp(self):
        self.Id = int(input("Enter emp id: "))
        self.Name = input("Enter emp name: ")
        self.Dept = input("Enter emp Dept: ")
        self.Sal = int(input("Enter emp Salary: "))

    def DisplayEmp(self):
        print("Emp id:", self.Id)
        print("Emp Name:", self.Name)
        print("Emp Dept:", self.Dept)
        print("Emp Salary:", self.Sal)

class Manager(Employee):
    def AcceptMgr(self):
        self.bonus = int(input("Enter Manager Bonus: "))

    def DisplayMgr(self):
        print("Manager Bonus is:", self.bonus)
        self.TotalSal = self.Sal + self.bonus
        print("Total Salary: ", self.TotalSal)

# Input for number of managers
n = int(input("Enter How many Managers: "))
lst = []

for i in range(n):
    print(f"\nEntering details for Manager {i + 1}:")
    mgr = Manager()  # Create an instance of Manager
    mgr.AcceptEmp()  # Accept employee details
    mgr.AcceptMgr()  # Accept manager details
    lst.append(mgr)  # Append the instance to the list

# Display details of each manager
for j in range(n):
    print(f"\nDisplay Details of Manager {j + 1}:")
    lst[j].DisplayEmp()
    lst[j].DisplayMgr()

# Logic to find the manager with maximum salary
maxTotalSal = lst[0].TotalSal
maxIndex = 0

for j in range(1, n):
    if lst[j].TotalSal > maxTotalSal:
        maxTotalSal = lst[j].TotalSal
        maxIndex = j

print("\nDisplay Details of Manager Having Maximum Salary (Salary + Bonus):")
lst[maxIndex].DisplayEmp()
lst[maxIndex].DisplayMgr()

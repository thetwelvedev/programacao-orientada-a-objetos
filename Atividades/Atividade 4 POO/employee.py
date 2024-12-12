from abc import ABC, abstractmethod
class Employee(ABC):
    def __int__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_responsibilities(self):
        pass

class Developer(Employee):
    def __init__(self, salario):
        self.salario = salario

    def calculate_salary(self, num_projetos):
        bonus = 100*num_projetos
        self.salario = self.salario  + bonus
        return print(f"O salário do Developer é R$ {self.salario:.2f}")
    
    def get_responsibilities(self):
        return print("Escrever código")

class Manager(Employee):
    def __init__(self, salario):
        self.salario = salario

    def calculate_salary(self, num_func_gerenciados):
        bonus = 200*num_func_gerenciados
        self.salario = self.salario + bonus
        return print(f"O salário do Manager é R$ {self.salario:.2f}")
    
    def get_responsibilities(self):
        return print("Gerenciar equipe")
    
class Project():
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            return "Não é uma uma instância da classe Employee"
    def calculate_total_cost(self):
        sum = 0
        for employee in self.employees:
            sum += employee.salario
        return print(f"Custo total do projeto: R$ {sum:.2f}")
    
    # def calculate_total_cost(self):
    #     total = sum(employee.salario for employee in self.employees)
    #     print(f"Custo total do projeto: R$ {total:.2f}")

if __name__ == "__main__":
    employee1 = Developer(5000)
    employee2 = Manager(8000)

    employee1.calculate_salary(10)
    employee1.get_responsibilities()
    employee2.calculate_salary(10)
    employee2.get_responsibilities()

    employees = [employee1, employee2]
    project = Project("Desenvolvimento de Software", employees)

    employee3 = Developer(4000)
    project.add_employee(employee3)
    project.calculate_total_cost()
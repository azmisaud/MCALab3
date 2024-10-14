def read_departments(filename):
    with open(filename,'r') as file:
        return {int(line.split(',')[0]):line.split(',')[1] for line in file}
    
def read_employee_salaries(filename):
    department_salaries={}

    with open(filename,'r') as file:
        for line in file:
            _,_,salary,did=line.strip().split(',')
            did=int(did)
            salary=float(salary)

            if did not in department_salaries:
                department_salaries[did]=[]
            department_salaries[did].append(salary)

    return department_salaries

def main():

    departments=read_departments('department.txt')
    departments_salaries=read_employee_salaries('employee.txt')
    print('Average salary : ')

    for did, dname in departments.items():
        if did in departments_salaries:
            salaries=departments_salaries[did]
            avg_salary=sum(salaries) / len(salaries)
            print(f'Department {dname} : {avg_salary:.2f}')
        else:
            print(f'Department {dname} : No employees')


if __name__=="__main__":
    main()

import multiprocessing
import time

def calculate(department):
    print(f"Calculating salaries for {department} department")
    time.sleep(2)
    print(f"Finished salary calculation for {department}")

if __name__ == '__main__':

    departments = ["HR", "Finance", "Engineering", "Sales"]
    processes = []

    for dept in departments:
        p = multiprocessing.Process(target=calculate,args=(dept,))

        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Payroll processing completed using multiprocessing.")

Calculating salaries for HR department
Calculating salaries for Finance department
Calculating salaries for Engineering department
Calculating salaries for Sales department
Finished salary calculation for HR
Finished salary calculation for Finance
Finished salary calculation for Engineering
Finished salary calculation for Sales
Payroll processing completed using multiprocessing.

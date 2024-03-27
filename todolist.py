tasks=[]
print("--------WELCOME TO THE TO_DO APP--------")
def addt():
    print("Enter the task ",len(tasks)+1,": ",sep="",end="")
    s=input()
    tasks.append(s)
    print("Task added successfully")

def delt():
    if (len(tasks)==0):
        print("There are no tasks to delete")
    else:
        n=int(input("Enter the task number to delete it: "))
        tasks.pop(n-1)
        print("Task removed successfully")
def view():
    if(len(tasks)==0):
        print("There are no tasks.")
    else:
        print("*********TASKS*********")
        for i in range(len(tasks)):
            print(i+1,". ",tasks[i],sep="")

while True:
    print("\n")
    print("Please select one of the options:")
    print("=================================")
    print("1. Add a new task")
    print("2. Drop a task")
    print("3. View tasks")
    print("4. Exit")

    choice=input("Enter your choice: ")

    if(choice=="1"):
        addt()
    elif(choice=="2"):
        delt()
    elif(choice=="3"):
        view()
    elif(choice=="4"):
        print("THANK YOU👋👋")
        break
    else:
        print("INVALID CHOICE..CHOOSE AGAIN")
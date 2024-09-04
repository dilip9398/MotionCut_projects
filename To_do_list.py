tasks = []


def Add_task():
    task = input("Enter you works to do :  ")
    tasks.append(task)
    print(f"Task {task} has be added.")

def delete_task():
    show_list()
    try:
        to_delete = int(input("Enter the # task to delete: "))
        if to_delete < len(tasks):
            tasks.pop(to_delete-1)
            print(f"Task {to_delete} has completed.")
        else:
            print(f"Task #{to_delete} is not found. ")
    except:
        print("Invalid input")
    

def show_list():
    if not tasks:
        print("No tasks!")
    else:
        print("Working tasks > ")
        for  jap ,task in enumerate(tasks, start=1):
           print(f"Task #{jap}.{task}")




if __name__ == "__main__":

    print("Welcome to super TO-Do-List. :)")
    while True:
        print("Get back to work!")
        print("-----------------")
        print("1. Add Tasks ")
        print("2. Remove Tasks ")
        print("3. show Tasks ")
        print("4. Quit ")

        choice = int(input("Choose the option: "))

        if choice == 1:
            Add_task()
        elif choice == 2:
            delete_task()
        elif choice == 3:
            show_list()
        elif choice == 4:
            break
        else:
         print("Invalid  Input")
    print("Come Back Again! To complete tasks (:")    

    

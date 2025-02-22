import datetime
import json

def main():
    
    tasks = []
    with open('Tasks.json', 'w') as file:  
        file.close()

    while True:
            
            task_id = 0
            current_data = datetime.datetime.now()
            print("\n===== To-Do List =====")
            print("1. Add Task")
            print("2. Update Task")
            print("3. Delete Task")
            print("4. Show Tasks")
            print("5. Save in JSON file")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                print()
                n_tasks = int(input("How many task you want to add: "))

                for _ in range(n_tasks):
                    task = input("Enter the task: ")
                    task_description = input("Add a little description: ")
                    task_id += 1   
                    createdAt = current_data.strftime('%d/%m/%y %H:%M:%S')
                    updatedAt = createdAt
                    task_status = "to-do"
                    tasks.append(dict(task_id = task_id, task = task, description = task_description,
                                       createdAt = createdAt, updatedAt = updatedAt, status = task_status))
                    print("Task successfully added!")

            elif choice == '2':
                print()
                task_to_update = int(input("Enter the task id, which task you want to update: "))
                for i in range(len(tasks)):
                    if i+1 == task_to_update:
                        change_task = tasks[i]
                        print(change_task)
                        print("\n===== To-Do List =====")
                        print("1. Mark as done")
                        print("2. Mark as in-progress")
                        print("3. Mark as to-do")
                        print("4. Return")

                        new_status = input("Choose task status: ")

                        if new_status == '1':
                            change_task['status'] = 'done'
                            change_task['updatedAt'] = current_data.strftime('%d/%m/%y %H:%M:%S')
                            print("Task status has changed")
                        elif new_status == '2':
                            change_task['status'] = 'in-progresss'
                            print("Task status has changed")
                        elif new_status == '3':
                            change_task['status'] = 'to-do'  
                            print("Task status has changed")
                        elif new_status == '4':
                            continue 
                        else:
                            print("Your input incorrect, please try again")
                            new_status = input("Choose task status: ")
                        
                        tasks[i] = change_task
 

            elif choice == '3':
                print()
                task_to_delete = int(input("Enter the task id, which task you want to delete: "))
                for i in range(len(tasks)):
                    if i+1 == task_to_delete:
                        del tasks[i]
                        print("Task successfully deleted!")

            elif choice == '4':
                print("\n===== To-Do List =====")
                print("1. Show all tasks")
                print("2. Show the tasks I have do")
                print("3. Show tasks in progress")
                print("4. Show the tasks that I have to do")
                print("5. Return")

                choice_2 = input("Enter your choice: ")

                if choice_2 == '1':
                    print("\n All tasks:")
                    if len(tasks) == 0:
                        print("In this moment you task list is empty")
                    for i in range(len(tasks)):
                        print(tasks[i], sep='\n')
                
                elif choice_2 == '2':
                    print("\n Completed tasks:")
                    task_has_done = [x for x in tasks if x['status'] == 'done']
                    if len(task_has_done) == 0:
                        print("In this moment you don't currently have any completed tasks")
                    for i in range(len(task_has_done)):
                        print(task_has_done[i], sep='\n')
                
                elif choice_2 == '3':
                    print("\n Tasks in progress:")
                    task_in_progress = [x for x in tasks if x['status'] == 'in-progress']
                    if len(task_in_progress) == 0:
                        print("In this moment you don't currently have tasks in progress")
                    for i in range(len(task_in_progress)):
                        print(task_in_progress[i], sep='\n')

                elif choice_2 == '4':
                    print("\n Need to start tasks:")
                    task_to_do = [x for x in tasks if x['status'] == 'to-do']
                    if len(task_to_do) == 0:
                        print("Right now you don't have any tasks that need to be started.")
                    for i in range(len(task_to_do)):
                        print(task_to_do[i], sep='\n')

                elif choice_2 == '5':
                    continue

                else:
                    print("Your input incorrect, please try again")
                    continue
            
            elif choice == '5':
                with open('Tasks.json', 'w') as file:
                    json.dump(tasks, file, ensure_ascii=False, indent=4, default=str)    
                    file.close() 
                    continue

            elif choice == '6':
                with open('Tasks.json', 'w') as file:
                    json.dump(tasks, file, ensure_ascii=False, indent=4, default=str)    
                    file.close() 
                break 

            else:
                print("Your input incorrect, please try again")
                continue

if __name__ == "__main__":
    main()
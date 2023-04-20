print("TODO LIST")
print("-----------------")
print("Welcome!")
print("Would you like to")
print("[A]dd a new task")
print("[D]elete a task")
print("[E]dit a task")
print("[V]iew all tasks")
print("[Q]uit the program")
print("")

todo_list = []
divider = ("-----------------")

while True:
    print("Choose An Option:")
    
    user_option = input("> ").upper().strip()

    # ADD an item
    if user_option == "A":
        print("what would you like to add?")
        add_todo = input("> ").upper().strip()
        
        while True:
            if add_todo == "":
                print("Nothing entered. Try again!")
                print("what would you like to add?")
                add_todo = input("> ").upper().strip()

            else:
                break
        
        if add_todo not in todo_list:
            todo_list.append(add_todo)
            print(f"{add_todo} added to todo list!")
            print(divider)

        else: 
            print(f"{add_todo} is already on your todo list")
            print(f"Are you sure you want to add {add_todo} another time?")
            print("(Y / N)")
            add_again = input("> ").upper().strip()

            while True:
                if add_again == "Y":
                    todo_list.append(add_todo)
                    print(f"{add_todo} added to todo list!")
                    print(divider)
                    break
                elif add_again == "N":
                    print("Nothing tasks were added.")
                    print(divider)
                    break
                else:
                    print("Try again with a valid selection! (Y / N)")
                    add_again = input("> ").upper().strip()

    # DELETE an item
    elif user_option == "D":
        
        if len(todo_list) >= 1:
            print("What would you like to delete?")
            delete_todo = input("> ").upper().strip()

            # check if entry is valid
            # "C" for cancel
            while True: 
                if (delete_todo in todo_list) or delete_todo == "C":
                    break
                else:
                    print("That item is not in the list")
                    print()
                    print("Choose from the following:")
                    print()
                    for i in todo_list:
                        print(i)
                    print("[C]ancel")
                    delete_todo = input("> ").upper().strip()
                    
            # Cancel if user changes mind
            if delete_todo == "C":
                print("Nothing deleted.")
                print(divider)
                
            elif delete_todo != "C":
                # check if item being deleted is in the list more than once.
                word_count = 0
        
                for i in todo_list:
                    if i == delete_todo:
                        word_count = word_count + 1
                        
                # if item being deleted is in list more than once, clarify which instance to delete        
                if (word_count > 1):
                    print()
                    print(f"{delete_todo} appears {word_count} times in todo_list: ")
                    print(f"Which {delete_todo} do you want to delete? (select number)")
                    print()
            
                    instance = 0
                    
                    for task in (todo_list):
                        if task == delete_todo:
                            instance = instance + 1
                            print(f"[{instance}] {task}")
                            
                        else:
                            print(task)
                            
                    print()        
                
                    # make sure user is entering a numeric value
                    while True:
                        
                        try:
                            delete_selection = int(input("> "))
                            
                            # if value entered is numberic, check to see if it is in the range of the # of instances
                            if delete_selection >=1 and delete_selection <= instance:
                                
                                new_instance = 0
        
                                # find/delete what they said to delete, break the loop
                                for i, item in enumerate(todo_list):
                                    if item == delete_todo:
                                        new_instance = new_instance + 1
            
                                        if new_instance == delete_selection:
                                            todo_list.pop(i)
                                            print(f"{delete_todo} removed from todo list")
                                            print(divider)
        
                                # breaks out of both the try/except block and while loop
                                break
                            else:
                                print("try again using a valid number")
                                continue
                                
                        except ValueError:
                            print("try again using a valid number")
                            continue

                # only instance in list deleted
                else:
                    for i, task in enumerate(todo_list):
                        if task == delete_todo:
                            todo_list.pop(i)
                    print(f"{delete_todo} deleted from list")
                    print(divider)
                    
        # nothing in list to delete
        else:
            print("No tasks to delete!")
            print(divider)

    # EDIT an item
    elif user_option == "E":

        # if list has items, ask which item the user would like to edit
        if len(todo_list) >=1:
            print("What task would you like to edit?")
            edit_selection = input("> ").upper().strip()
            
            counter = 0

            # check if there are duplicates in list
            for i in todo_list:
                if i == edit_selection:
                    counter = counter + 1

            # if duplicates, clarify which instance to edit
            if counter > 1:
                print()
                print(f"{edit_selection} appears {counter} times")
                print("Which instance would you like to edit?")
                print()

                new_counter = 0

                for item in todo_list:
                    if item == edit_selection:
                        new_counter = new_counter + 1
                        print(f"[{new_counter}] {edit_selection}")
                    else:
                        print(item)
                        
                print()
                selection = input("> ").upper()

                # ask for a valid entry 
                #BUG***** - how do I get the else statement to catch anything that is not an int?
                while True:

                    if (int(selection) >= 1) and (int(selection) <= counter):
                        print("Got it!")
                        break

                    else:
                        print("try again using a valid selection!")
                        print("Which instance would you like to edit?")
                        selection = input("> ")

                                          
                print("What would you like to replace it with?")
                replace_selection = input("> ").upper().strip()

                # If task user wants to replace is already in list, ask them if they are sure
                if replace_selection in todo_list:
                    print(f"{replace_selection} is already in the todo list")
                    print(f"do you still want to edit {edit_selection} to {replace_selection}?")
                    print("(Y / N)")
                    replace_choice = input("> ").upper().strip()
                        
                    while True:
                        if replace_choice == "Y":
                            for i, edit in enumerate(todo_list):
                                if edit == edit_selection:
                                    todo_list[i] = replace_selection
                            print(f"replaced {edit_selection} with {replace_selection}")
                            print()
                            break
    
                        elif replace_choice == "N":
                            print("Nothing was added.")
                            print()
                            break
    
                        if (replace_choice != "Y") or (replace_choice != "N"):
                            print("Try again with a valid selection! (Y / N)")
                            replace_choice = input("> ").upper().strip()
                            
                # if task user wanted to enter is not in list, edit taks
            elif (replace_selection not in todo_list) and (replace_selection != "N"):    
                print("That item is not in the list!")
                print("Choose from the following:")
                print()
                for i in todo_list:
                    print(i)
                print()
                
        # if not items in list, do nothing
        else:
            print("No items on your todo_list")
            print()
            
    # VIEW todo list 
    elif user_option == "V":

        if len(todo_list) >=1:
            print()
            print("TODO:")
            print("-----")
            
            for i in todo_list:
                print(i)
            print()
            print(divider)
        else:
            print("No items on your todo list!")
            print(divider)

    elif user_option == "Q":
        
        print("Are you sure you want to exit? (Y / N)")
        choice = input("> ").upper().strip()

        while True:
            if (choice == "Y") or (choice == "N"):
                break
            
            if (choice != "Y") or (choice != "N"):
                print("Try again with a valid selection! (Y / N)")
                choice = input("> ").upper().strip()
                

        if choice == "Y":
            print("Goodbye!")
            break

        elif choice == "N":
            print(divider)
        
    
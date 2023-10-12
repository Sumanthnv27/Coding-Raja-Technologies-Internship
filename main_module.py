def main():
 file1=open("details_file.text","a")
 file1.close()
 file2=open("due_date_file.text","a")
 file2.close()
 file3=open("priority_file.text","a")
 file3.close()
 import os
 p=os. path. getsize("details_file.text") == 0
 if(p==True):
      details_dict={}
      due_date_dict={}
      pririty_dict={}
      file1=open("details_file.text","a")
      file1.write(str(details_dict))
      file1.close
      file2=open("due_date_file.text","a")
      file2.write(str(due_date_dict))
      file2.close
      file3=open("priority_file.text","a")
      file3.write(str(pririty_dict))
      file3.close
 while True:
    print("Select operation.")
    print("1.add_task")
    print("2.add_due_date")
    print("3.add_pririty")
    print("4.mark_complete")
    print("5.display")   
    print("6.remove")
    choice = input("Enter choice(1/2/3/4/5/6): ")
    if choice in ('1', '2', '3','4','5','6'):
        if choice == '1':
            from add_task_module import add_task
            add_task()
        elif choice=="2":
            from add_due_date_module import add_due_date
            add_due_date()
        elif choice=="3":
            from add_priority_module import add_priority
            add_priority()
        elif choice=="4":
            from mark_complete_module import complete
            complete()
        elif choice=="5":
            from display_module import display
            display()
        elif choice=="6":
            from remove_module import remove
            remove()
        next_calculation = input("Do want to stay (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
main()
def add_due_date():
  import ast
  with open("details_file.text","r") as j:
      det_dict=ast.literal_eval(j.read())
  p=len(det_dict)
  if(p==0): 
        print("There are no tasks pls add first")
  else:
    with open("details_file.text","r") as j:
      det_dict=ast.literal_eval(j.read())
    file_li=list(det_dict)
    print(f"The tasks available are {file_li}")
    print("enter the task  to enter due date")
    task=input()
    with open("due_date_file.text","r") as j:
      due_dict=ast.literal_eval(j.read())
    print(f"Enter the due date for {task}:")
    due_dict[task]=input("due_date:")
    file=open("due_date_file.text","w")
    file.write(str(due_dict))

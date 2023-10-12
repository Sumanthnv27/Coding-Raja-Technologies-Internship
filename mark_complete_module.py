def complete():
  import ast
  with open("details_file.text","r") as j:
      det_dict=ast.literal_eval(j.read())
  p=len(det_dict)
  if(p==0): 
        print("There are no tasks pls add first")
  else:
    import ast
    with open("details_file.text","r") as j:
      det_dict=ast.literal_eval(j.read())
    file_li=list(det_dict)
    del_task=input(f"The tasks available are {file_li}")
    print("Enter the task number to mark completed")
    comp=input()
    with open("due_date_file.text","r") as j:
      due_dict=ast.literal_eval(j.read())
    due_dict[comp]="Completed"
    file=open("due_date_file.text","w")
    file.write(str(due_dict))
    print("The tsk status successfully updated")
def remove():
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
    del_task=input(f"The tasks available are {file_li} \n Enter the task to delete:")
    import ast
    with open("details_file.text","r") as j:
      det_dict=ast.literal_eval(j.read())
    with open("due_date_file.text","r") as j:
      due_dict=ast.literal_eval(j.read())
    with open("priority_file.text","r") as j:
        prior_file=ast.literal_eval(j.read())
    del  det_dict[del_task]
    del  due_dict[del_task]
    del prior_file[del_task]
    file=open("details_file.text","w")
    file.write(str(det_dict))
    file=open("due_date_file.text","w")
    file.write(str(due_dict))
    file=open("priority_file.text","w")
    file.write(str(prior_file))
    print(f"task {del_task} is deleted sucessfully")
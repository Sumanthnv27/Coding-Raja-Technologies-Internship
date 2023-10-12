def add_priority():
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
    print("enter the task  no to add priority")
    task=input()
    with open("priority_file.text","r") as j:
        prior_file=ast.literal_eval(j.read())
    print(f"Enter the priority for task {task} ")
    prior_file[task]=input("enter medium or low Or high :")
    file=open("priority_file.text","w")
    file.write(str(prior_file))
def display():
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
    with open("due_date_file.text","r") as j:
      due_dict=ast.literal_eval(j.read())
    with open("priority_file.text","r") as j:
        prior_file=ast.literal_eval(j.read())

    for i in det_dict.keys():
      print("_______________________________________________________________________________________________")
      print(f"{i}:" )
      details=det_dict[i]
      print(details[0])
      print(f"due_date:" f"{due_dict[i]}")
      print(f"priority:" f"{prior_file[i]}")
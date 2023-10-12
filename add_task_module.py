def add_task():
    import ast
    with open("details_file.text","r") as j:
      det_dict=ast.literal_eval(j.read())
    file_li=list(det_dict)
    import os
    p=os. path. getsize("details_file.text") == 0
    if(p==False):
         len1=len(file_li)
         tno=len1+1
         task=f"task {tno}"
    else:
      i=1
      task=f"task {i}"
    print(f"Enter the {task} details:")
    taskli=[]
    taskli.append(input())
    det_dict[task]=taskli
    file=open("details_file.text","w")
    file.write(str(det_dict))
    # with open("priority_file.text","r") as j:
    #     prior_file=ast.literal_eval(j.read())
    # print(f"Enter the priority for task {task} ")
    # prior_file[task]=input("enter medium or low Or high :")
    # file=open("priority_file.text","w")
    # file.write(str(prior_file))
def Sorting_my_list(my_list,sorting_criteria="age",sorting_order="ascending"):
    """This function is used to sort the given list"""
    if sorting_order=="Ascending" or sorting_order=="ascending":
        if sorting_criteria=="Age" or sorting_criteria=="age":
            for i in range(len(my_list)):
                for j in range(len(my_list)):
                    if my_list[i][0]<my_list[j][0]:
                        my_list[j],my_list[i]=my_list[i],my_list[j]
            return my_list
     
        elif sorting_criteria=="GPA" or sorting_criteria=="gpa" or sorting_criteria=="Gpa":
            for i in range(len(my_list)):
                for j in range(len(my_list)):
                    if my_list[i][1]<my_list[j][1]:
                        my_list[j],my_list[i]=my_list[i],my_list[j]
            return my_list
     
        elif sorting_criteria=="City" or sorting_criteria=="city":
            for i in range(len(my_list)):
                for j in range(len(my_list)):
                    if my_list[i][2]<my_list[j][2]:
                        my_list[j],my_list[i]=my_list[i],my_list[j]
            return my_list
     
        else:
            print("Error Invilide Sorting Criteria")
            return my_list
    

    elif sorting_order=="Descending" or sorting_order=="descending":
        if sorting_criteria=="Age" or sorting_criteria=="age":
            for i in range(len(my_list)):
                for j in range(len(my_list)):
                    if my_list[i][0]>my_list[j][0]:
                        my_list[j],my_list[i]=my_list[i],my_list[j]
            return my_list
    
        elif sorting_criteria=="GPA" or sorting_criteria=="gpa" or sorting_criteria=="Gpa":
            for i in range(len(my_list)):
                for j in range(len(my_list)):
                    if my_list[i][1]>my_list[j][1]:
                        my_list[j],my_list[i]=my_list[i],my_list[j]
            return my_list
    
        elif sorting_criteria=="City" or sorting_criteria=="city":
            for i in range(len(my_list)):
                for j in range(len(my_list)):
                    if my_list[i][2]>my_list[j][2]:
                        my_list[j],my_list[i]=my_list[i],my_list[j]
            return my_list
    
        else:
            print("Error Invilide Sorting Criteria")
            return my_list
    

    else:
        print("Error Invilide Sorting Order")
        return my_list

mylist=[[29, 3.2, 'Rawalpindi'], [22, 4.0, 'Islamabad'], [12, 0, 'Karachi']]

sort_criteria=str(input("Eenter criteria Order(age,gpa,city)"))
sort_order=str(input("Eenter Sorting Order(ascending,descending)"))

for i in mylist:
    print(f"Age={i[0]}|GPA={i[1]}|City={i[2]}")

print("-------------------")
print("After Sorting")

for i in Sorting_my_list(mylist,sort_criteria,sort_order):
    print(f"Age={i[0]}|GPA={i[1]}|City={i[2]}")
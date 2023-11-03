'''
Have the function FindIntersection(strArr) read the array of strings 
stored in strArr which will contain 2 elements: the first element will 
represent a list of comma-separated numbers sorted in ascending order, 
the second element will represent a second list of comma-separated 
numbers (also sorted). Your goal is to return a comma-separated string 
containing the numbers that occur in elements of strArr in sorted order. 
If there is no intersection, return the string false.

Examples:
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13

Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10
'''


def FindIntersection(strArr):
  
  int_list_a = []
  int_list_b = []
  
  # Formating text string arrays into integer arrays
  for i in strArr[0].split(", "):
    int_list_a.append(i)

  for i in strArr[1].split(", "):
    int_list_b.append(i)

  for i in range(len(int_list_a)):
    int_list_a[i] = int(int_list_a[i])

  for i in range(len(int_list_b)):
    int_list_b[i] = int(int_list_b[i])
  
  # Build intersection
  int_list_c = list(set(int_list_a) & set(int_list_b))

  # Formating the output to text string
  if int_list_c == []:
    return "false"
  
  else:
    int_list_c.sort()
    return int_list_c
  

# Otra solución
def FindIntersection(strArr):

    set_a = set(strArr[0].split(", "))
    set_b = set(strArr[1].split(", "))

    inters_list = list(set_a & set_b)

    # Formating (str > int) for sorting 
    for i in range(len(inters_list)):

        inters_list[i] = int(inters_list[i])

    if inters_list == []:

        return False
    
    else:

        inters_list.sort()

        return inters_list


# CONVERTIR SERIE DE NÚMEROS EN FORMATO TEXTO A SERIE NÚMEROS EN FORMATO ENTEROS:
str_list = ['1, 4, 13']
new_list = [int(i) for i in str_list[0].split(", ")]
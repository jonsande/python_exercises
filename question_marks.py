'''
Have the function QuestionsMarks(str) take the str string parameter, 
which will contain single digit numbers, letters, and question marks, 
and check if there are exactly 3 question marks between every pair of 
two numbers that add up to 10. If so, then your program should return 
the string true, otherwise it should return the string false. If there 
aren't any two numbers that add up to 10 in the string, then your program 
should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should 
return true because there are exactly 3 question marks between 6 and 4, 
and 3 question marks between 5 and 5 at the end of the string.
'''


def QuestionsMarks(strParam):

  clean_str = ''
  for i in strParam:
      if not i.isalpha():
          clean_str += i

  sum = 0
  counter = 0

  while len(clean_str) >= 5:

      index = clean_str.find('???')

      if index >= 1:
          try:
              sum = int(clean_str[index - 1]) + int(clean_str[index + 3])
              if sum == 10:
                  return True
              else:
                  sum = 0
                  clean_str = clean_str[index + 4:]
                  
          except ValueError:
              return False

      else:
          return False

  return False
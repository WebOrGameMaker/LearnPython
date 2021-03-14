def get_student_names(dct):
  """

  >>> get_student_names({"Student 1" : "Steve", "Student 2" : "Becky", "Student 3" : "John"})
  ['Becky', 'John', 'Steve']
  """
  lst_values = list(dct.values())
  lst_values.sort()
  return lst_values
  
if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
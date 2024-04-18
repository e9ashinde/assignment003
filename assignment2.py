def read_and_print(filename):
  with open("file.txt",'r') as f:
    data=f.read()
    return data

print(read_and_print('/home/sierra/repository/python-jobs/assignment003/file.txt'))
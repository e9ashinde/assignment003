def read_and_print(filename):
  with open(filename,'r') as f:
    data=f.read()
    return data
  
print(read_and_print('/home/sierra/repository/assignment003/file.txt'))


def read_and_count(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
            count = 0
            for line in data:
                if not line.startswith('T'):
                    count += 1
            return f"Number of lines not starting with 'T': {count}"
    except FileNotFoundError:
        return "File not found!"

print(read_and_count('/home/sierra/repository/assignment003/file.txt'))

def count_words(filename):
    d={}
    with open(filename,'r') as f:
        data=f.readlines()
        for line in data:
            words=line.split(' ')
            for word in words:
                cnt=words.count(word)
                d[word]=cnt
    return d

print(count_words('/home/sierra/repository/assignment003/file.txt'))


def count_the(filename):
    c=0
    with open(filename,'r') as f:
        data=f.readlines()
        for line in data:
            words=line.split(' ')
            for word in words:
                if word=='the':
                    c+=1
    return c

print(count_the('/home/sierra/repository/assignment003/file.txt'))


def display_words(filename):
    with open(filename,'r') as f:
        l=[]
        data=f.readlines()
        for line in data:
            words=line.split(' ')
            for word in words:
                if len(word)<4:
                    l.append(word)
        return l
    
print(display_words('/home/sierra/repository/assignment003/file.txt'))


def count_words(filename):
    with open(filename,'r') as f:
        c1=0
        c2=0
        data=f.readlines()
        for line in data:
            words=line.split(' ')
            for word in words:
                if word=='this':
                    c1+=1
                elif word=='these':
                    c2+=1
        return f'this:{c1},these:{c2}'
    
print(count_words('/home/sierra/repository/assignment003/file.txt'))


def count_ewords(filename):
    with open(filename,'r') as f:
        c1=0
        data=f.read()
        for line in data:
            words=line.split(' ')
            for word in words:
               if word.endswith('e'):
                   c1+=1
        return f'The count of words end with e is {c1}'
    
print(count_ewords('/home/sierra/repository/assignment003/file.txt'))


def count_upper(filename):
    with open(filename,'r') as f:
        data=f.read()
        upper=0
        for letter in data:
            if letter.isupper():
              upper+=1
        return upper
              
print(count_upper('/home/sierra/repository/assignment003/file.txt'))


def hash_display():
    with open('/home/sierra/repository/assignment003/file.txt','r') as f:
        data=f.read()
        for i in data:
            print(i,end="#")
            
print(hash_display())
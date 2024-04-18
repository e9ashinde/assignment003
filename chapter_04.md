# Control Flow Tools
 

** Conditional statements:**

     If statement is used to check if value is true then print otherwise 
     go to else 

     Use of elif : In python's way says that if condition is wrong then 
     try elif 


**for loop and while loop:** 

      for loop is used when the number of iterations is known, 
      whereas 
      execution is done in the while loop until the statement in the 
      program is proved wrong.

**The range() function:**
     
       range() is a generator type function it generates the sequence in the given range.
       
       ex. list(range(4))
           It will produce the list of 4 elements like [0,1,2,3]


**break,continue and pass statements:**

      break: breaks the current enclosing loop
      pass : nothing
      continue: It skips the current iteration and continue the loop from the next statement


**match statements:**

      Match-Case is the Switch Case of Python. Here we have to first pass a parameter then try to check with which case the parameter is getting satisfied. If we find a match we will do something and if there is no match at all we will do something else.


**Defining function:**

    Function is a block of code which only runs when it call.

    There are two type of function in python :

           1. User defined function = The functions which defined by user by def keyword

           Ex. def add(a,b):
                   return a+b
               print(add(3,4))

           2. built-in function = function which already exist in python

           Ex. print(pow(2,3))

**Lambda Expression:** 

     lambda is an expression which allows us to make an anonomous    
     function. It is one liner function.

     Ex. lst=[1,2,3]
         list(map(lambda x:x*3,lst))

         In above example it will create list of numbers in lst 
         multiplied by 3 
# Data Structures

The list data type has some more methods.

        1. append() : It will append the element at the end of the   
                      existing list.

           Ex. lst=[1,2,3]
               lst.append(4)
               print(lst)
           Ans: [1,2,3,4]

        2. extend(): It will extend the existing list by adding the 
                     elements in list to the existing list.

            Ex. lst=[1,2,3]
                lst.extend([4,5])
                print(lst)
            Ans: [1,2,3,4,5]
        
        3.insert(): It will insert the element at specific position.

            ex. lst=[1,2,3]
                lst.insert(4,8)
                print(lst)
            Ans: [1,2,3,8]
        4. remove(x): Remove the first item from the list whose value is 
                     equal to x.
            Ex. lst.remove(2)
             
        5. pop(): by default remove the last element from list.
           Ex. lst.pop()

        6. clear(): Remove all items from the list.

        7. count(x): Return the number of times x appears in the list.

        8. reverse(): Reverse the elements of the list in place.
                      In place of reverse function we can use lst[::-1].


**Using list as queues:**

        It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”).
        we can import deque by using from collections import deque

**List Comprehension:** It is concise way to create a list.

            Ex. lst=[i for i in range(10)]
                print(lst)

**Tuples:** 

     It ia ordered collection of an elements stored in paranthesis but 
     it is an optional.
     
     Ex. tup=(10,)
         print(tup)

**Dictionary:**

     It is an unordered collection of elements in the form of key value 
     pairs.

     Ex. d={"A":"Apple,"B":"Ball","C":"Color"}
         print(d)

         if we want keys then use d.keys()
         for values use d.values()

**Set:**  It is an unordered collection of unique elements.
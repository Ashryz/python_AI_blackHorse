# python_AI_blackHorse

# RoadMap
## Python Fundamental 
- datatypes
- control flow
- arthimetic operation 
- data structure
- functions 
- oop

## DA 
- Pandas
- NumPy
- Matplotlib
- Seaborn

## ML
- scikit-learn (sklearn)

### session one 
- Data Types 
    - Integer    --> whole number (+n , -n, 0) but can't be a fraction or a decimal --> 1 , -1 , 0 
    - Float      --> decimal number > 1.5, -1.25, 0.75
    - Boolean    --> True,False
    - String     --> sequence of characters (letters, numbers, symbols, spaces) inside quotes --> "test",'12345',"""text & print !"""
    - List       --> collection of items inside [] squere brackets -->  [3, 4.5, 'text', True]
    - Tuple      --> collection of items inside () parentheses --> (2, 3, 4)
    - Set        --> collection of unique items inside {} curly brackets -->{"apple", "banana", "cherry"}
    - Dictionary --> collection of key–value pairs {} inside curly brackets --> {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
### session two
- Variables --> is container or name which refer to the value stored in memory
    - naming 
        - must start with a letter or the underscore character (A-z, _ )
        - name can only contain alpha-numeric characters and underscores  
        - case-sensitive (name, Name, NAME) all three different variables
        - cannot start with a number
        - cannot be any of the Python Reserved keywords.
    - naming techniques
        - camel case --> each word starts with capital letter except the first one --> (myVariableName)
        - pascal case --> each word starts with capital letter --> (MyVariableName)
        - snake case --> each word is separated by underscores --> (my_variable_name)
    - multiple values
        - many values to multiple variables --> x, y, z = "Orange", "Banana", "Cherry"
        - one value to multiple variables --> x = y = z = "Orange"
- string
    - index
    - slicing
    - negative slicing *
    - string format *
    - strip  --> remove spaces from right and left of string 
    - replace --> replaced old char_with new_char
    - split --> split string with (' ') or ('any char')
    - concatination  --> adding two or more string 

### session three
- slicing with step  -> [start:end:steps]
- negative slicing  -> [-5:-2]
- string format
- input
- arithmetic operation ->  +, -, *, /, //, %, **
- Data Structure
    - list []
        - len()   -> get length of list items
        - access  -> access list index               -> list[index]
        - slicing -> get list items using slicing    -> list[start:end]
        - insert  -> adding item by its index        -> list.insert(index, value)
        - append  -> adding item at the end of       -> list.append(value)
        - extend  -> adding list to my list          -> list.extend([value,value,value])
        - remove  -> remove item from list by value  -> list.remove(value)
        - pop     -> remove item from list by index  -> list.pop(index)
        - del     -> delete the list from memory
        - clear   -> make the list empty 
        - sort    -> arrange the list items    if reverse= True -> DESC
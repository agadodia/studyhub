Data Types - Integer, Long, Float, Boolean, String.
Primitive Data Type - Built in with no modification
Composite Data Tyoe - Combines Mutltiple datatypes

Mutable Datatypes - those whose values can be changed in place ex.List,Set,Dictionay,Byte array
Immutable Datatypes - those that can never change their value in place ex.Integers,Floats,complex,strings,Tuples,Frozen sets.
Strings are immutable. When you concatenate, add strings or manipulate them you create a new string.

Python Mutable and immutable objects are handled differently. Immutable objects are quicker to access and expensive to change because it involves the creation of a copy. Whereas mutable objects are easy to change.

Variables in Python:
-Can only contain letters, numbers and underscores.
-Cannot begin with a number
-Cannot be a keyword in python.

Identifiers in python:
-Cannot start with a number
-Keywords cannot be used
-Special symbols like !,@,<#,$ and % cannot be used
-Can be any length

Both an identifier and a variable are the names allotted by users to a particular entity in a program. The identifier is only used to identify an entity uniquely in a program at the time of execution whereas, a variable is a name given to a memory location, that is used to hold a value

Collections- 
Arrays - Same DataType, Adjacent to each other in memory
Vector - 
Lists - Can be diffdatatype, can have dups, can be accesses using index.A Python list is ordered because each new item is added to the end of the list
Set
Queue
Deque (Double ended Queue_
Hashes
Dictionaries

Conditionals - Conditional statements in Python. If a certain condition is true we execute a statement block otherwise you can have an else block. Indentation is very necessary in Python. Without correct indentation you would get a syntax error.  For multiple conditions to be check you can also use elif which stands for elseif . 
if (condition) :
	print("hello")
else :
	print("hi")

Switches - Multiple possible cases ofvalue
switch(sign):
	case "stop": pressBreak()
	case "exit": decelerate()
	default: ignore()

Loops - Loops run a block of code repeatedly. There are two types of loops : for and while. ex. 
For loops - reads for each element in <things>.For loops and lists work well together. ex.

for name in names:
	newName = capitalize(name)
	print newName

while loops - A while loop runs a code block until a condition returns false.
-can run indefinitely, so a condition is required to stop it. Commonly an iterative counter is used.
while n > 0:
	print(n)
	n=-1
while n > 0:
	if n==2:
	print("n is 2")
	break
print("Out of while")


-------------------------------------------------------------------
Lists -  A list is a collection of values in a specific order. The values do not have to be the same type.

-Are mutable datatypes.
-Can contain multiple datatypes(strings,floats,ints and also other lists)
-Denoted with brackets on each end ex.[1,"ab"]
-Can have any number of items including zero.
-To access specific third element use -> myList[2] 

-------------------------------------------------------------------------
Dictionaries - A dictionary is a collection of key-value pairs, where the value is accessed by using the key.
-Are mutable datatypes. But they have keys which must be immutable.
-Can be nested
-A value can be retrieved by using key ex. myDict["key"]

----------------------------------------------------------------------------
Input function - used to take input from user.
ex. input("Enter name: ")



Some of the popular editors that can be used for python programming:
Microsoft Visual Studio Code
Sublime text
Vi or Vim 
nano
GNU emacs
Notepad++
TextEdit


Compiled and Interpreted languages.
Compiled languages - where the code is all compiled at once and then run ex.Java, C 
Interpreted Languages - Where the code is interpreted line by line as it is running ex. Python, Javascript and Ruby

Functions - 
-Have a name.
-Called by adding parenthesis after the name (may or may not include parameters)
ex: def <function name>(arg):
	<things to do>
-Does something useful. can be called multiple times by just a single line instead of repeating the entire block of code.
-Can return a value
-Can accept value(s) as input
-If a composite data type was created that can be returned as well
-Inbuilt functions can be used as well. Ex. print(), open(),sum(),dict().

Functions can be put into modules an dmodules can be put in libraries to import large programs.
Python std library - has commonly used functions
-has time(time) function, gettingsystem information(sys),querying operating system(os) etc
-OS module is part of std python library. Programs that use OS module are generally more portable between different platforms
Some commands to get info on host operating system are:
-getlogin - returns name of logged user
-getgrouplist - returns a list of groupid that user belongs to
-getenv - returns the value of the environment variable that is passed to it
-uname - returns informatio to identify the current OS
-system - is used to run commands ina subshell of the system
Common functions for files:
-chown-changes the ownership of a file
-chmod - changes the access permissions of a file
-remove - removes the file at a given path
Common functions in OS modules for dir:
-getcwd - gets the current working directory
-listdir - lists the contents of the current dir
-mkdir - creates anew dir.

some common examples using the os module:
os.system("adduser newuser") linux cmd to add user os.system("powershell.exe")for windows only
os.system("whoami")-linux cmd
os.getcwd


 
----------------------------------------------
File Handlers
-Use built-in open() function
-Two arguments both strings - the path to the filenad file mode(read or write)
-returns a file handler object that represents the file.
-must be closed after use by calling .close()
---------------------------------------------------------
Exceptions handling:
-done using try/except block


Exceptions in Python:
-Raises an error
-Could be because 
	-Referencing a var by incorrect name
	-Dividing a number by zero
	-trying to read a file which does not exist
-result in stack trace(listing ways that something went wrong)

-----------------------------------------------------------------------
Useful functions in te JSON module are:
-dump and dumps : turn various kinds of structured data into a string which can be written to a file
-load and loads : turn a string back into structured data.

What is pip?
pip is the package manager for python and similar to apt in linux.
-used to install third party packages
-holds python modules that you can use in your code
-installed along with python
-called from the commandline and not within python.

--------------------------------------------------------





-------------------------------------------------
Commenting in Python - 
# symbol is used at the start of each line to be commented




----------------------------------------------------

Version Control 
-Tracks versions of your code as you update them
-Can be done locally on your computer or remotely as well
-Helps with collaboration when multiple people are working on the same project.
-Helps with security and error checking.

Common Version control Tools
-Git and Git Hub
-GNU arch
-Mercurial
Git is used commonly to perform these tasks:
-Add files to the repository
-Edit files in a Git repository
-Clone the existing repository
-Create and merge branches
-Rewrite history in a Git Repository
-Resolve merge conflicts

GitHub as the name suggests is a repository hosting service. Same commands that you use in terminal can be used here.

--------------------------------------------------------------------
Debugging in Python
Static Analysis - Can help catch common Syntax and semantic errors.
Dynamic Analysis -Done by analysing running applications . Using debugger to go line by line.


Assertions - Dynamic analysis uses assertions in runtime to raise errors.
Log Monitoring - keep track of errors in a running program. log files should capture all information when error occurs including all arguments, exception, traceback object.
Log monitoring tools- In Python the default, natice log monitoring tool is the library logging.
 - to get access to the library : import logging at the top
 - to save output into a file : add a line before you use the logging library.
logging.basicConfig(filename="app.log",level=logging.DEBUG)
--------------------------------------------------------------------
Testing in Python

Acceptance tests - Formalized tests that consider user needs, business needs and if the software is ready for final delivery.
System tests - A complete and integrated application is tested to see whether software meets specific requirements.
Integration tests - Individual units are combined and tested as a group. Interaction between different parts of software is tested here.
Unit tests - Smallest testable part of any software ex. function

-------------------------------------------------------------------
What is a REST API 

An API (Application Programming Interface) is a set of rules that are shared by a particular service. These rules determine in which format and with which command set your application can access the service, as well as what data this service can return in the response. The API acts as a layer between your application and external service. You do not need to know the internal structure and features of the service, you just send a certain simple command and receive data in a predetermined format.

REST API (Representational state transfer) is an API that uses HTTP requests for communication with web services.
It must comply with certain constraints. Here are some of them:

    Client-server architecture – the client is responsible for the user interface, and the server is responsible for the backend and data storage. Client and server are independent and each of them can be replaced.
    Stateless – no data from the client is stored on the server side. The session state is stored on the client side.
    Cacheable – clients can cache server responses to improve performance.
Types of Requests

Types of Requests or HTTP Request Methods characterize what action we are going to take by referring to the API.

In total, there are four main types of actions:

    GET: retrieve information (like search results). This is the most common type of request. Using it, we can get the data we are interested in from those that the API is ready to share.
    POST: adds new data to the server. Using this type of request, you can, for example, add a new item to your inventory.
    PUT: changes existing information. For example, using this type of request, it would be possible to change the color or value of an existing product.
    DELETE: deletes existing information

Status Codes

Status codes are returned with a response after each call to the server. They briefly describe the result of the call. There is a large number of status codes, we give those that you will most often meet:

    200 – OK. The request was successful. The answer itself depends on the method used (GET, POST, etc.) and the API specification.
    204 – No Content. The server successfully processed the request and did not return any content.
    301 – Moved Permanently. The server responds that the requested page (endpoint) has been moved to another address and redirects to this address.
    400 – Bad Request. The server cannot process the request because the client-side errors (incorrect request format).
    401 – Unauthorized. Occurs when authentication was failed, due to incorrect credentials or even their absence.
    403 – Forbidden. Access to the specified resource is denied.
    404 – Not Found. The requested resource was not found on the server.
    500 – Internal Server Error. Occurs when an unknown error has occurred on the server.

Endpoints

An Endpoint is a specific address (for example, https://weather-in-london.com/forecast), by referring to which you get access to certain features/data (in our case – the weather forecast for London). Commonly, the name (address) of the endpoint corresponds to the functionality it provides.
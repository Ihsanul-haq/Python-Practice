import sys
def main():
    #check for correct number of arguments
    if len(sys.argv)!=2:
        sys.exit("Too few command-line arguments" if len(sys.argv)<2 else "Too many command-line arguments")
    filename = sys.argv[1]
        #file must end with .py
    if not filename.endswith(".py"):
            sys.exit("Not a python file")
    try:
         with open(filename, "r") as file:
              lines = file.readlines()
    except FileNotFoundError:
         sys.exit("File does not exist")
    code_lines = 0
    in_docstring = False
    for line in lines:
         stripped = line.strip()
         #print(len(stripped))
         if not stripped:
              continue
         if stripped.startswith("'''") or stripped.startswith('"""'):              
              if in_docstring:               
                   in_docstring = False
              else:
                   in_docstring = True
              if stripped.endswith("'''") or stripped.endswith('"""') and len(stripped)>3:
                   in_docstring = False
              continue
         if in_docstring:
              continue
         if stripped.startswith("#"):
              continue   
         code_lines += 1  
    print(code_lines)
main()
    
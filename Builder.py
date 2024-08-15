import os 
import subprocess

class buildTool:
    def __init__(self) -> None:
        #the path from which the program is executed
        self.program_path=os.getcwd()

        #Error loging file path
        self.errorFile_path= f"{self.program_path}\\Err.txt"

        #Project path
        self.original_path=""

        #Include folder inside project if it exists
        self.include_path=""

        #Output file Path and name
        self.output_name="output"
        self.output_path=""

        #To enable building only if the path is correct
        self.buildFlag=False



    #runButton Method 
    def runOutput(self):
        #Run .exe output
        os.system(f"start cmd /k \"\"{self.output_path}\"\"")



    #Check directory Directory 
    def checkDir(self):
        #Check if the user selected a directory
        if(not os.path.exists(self.original_path)):
            self.buildFlag=False
            return False
        else:
            self.buildFlag=True
            os.chdir(self.original_path)
            self.include_path=self.original_path+"\\include"
            ls_list=os.listdir('.')

            #intialize the Lists contaning C/C++ files to build
            self.c_list= [item for item in ls_list if item.endswith(".c")]
            self.cpp_list= [item for item in ls_list if item.endswith(".cpp")]

            return True



    #Opening folder when clicking Show in Folder
    def openFolder(self):
        try:
            #Open Current Directory
            os.system("start .")
            return True
        except:
            return False    
        
    

    #build using GCC     
    def build(self,chosenName):
        if self.buildFlag :   
            #Check if output name is valid
            if self.validateFileName(chosenName):
                return "Please choose valid filename"
            # Output path inside created folder Build
            self.output_path=f"{self.original_path}\\Build\\{self.output_name}.exe"

            # Check if the project is C project or C++ Project
            self.CheckProject()

            #Call function to check
            self.CheckOutputExists()

            #Build project Command
            self.build_cmd=f"{self.build_cmd} -o \"{self.output_path}\" "

            #Build the project
            try:
                subprocess.check_output(self.build_cmd, shell=True, text=True)
                return f"\"{self.output_name}.exe\" Build Complete"
            except subprocess.CalledProcessError as e:
                return "Error"

        else:    
            return "Please choose a valid directory"



    #Check if output exists and delete it before building
    def CheckOutputExists(self):
        if(os.path.exists(self.output_path)):
            os.remove(self.output_path)
        else:
            try:
                os.mkdir("Build") 
            except(FileExistsError):
                pass
 


    #Check if the project is C or C++ project 
    def CheckProject(self):
        if(len(self.cpp_list)):
            self.build_cmd= f"g++ -I\"{self.include_path}\" "
            for item in self.cpp_list :
                #Append C++ files to g++ command
                self.build_cmd= self.build_cmd + " " + item
        else:
            self.build_cmd= f"gcc -I\"{self.include_path}\" "
            for item in self.c_list :
                #Append C files to gcc command
                self.build_cmd= self.build_cmd + " " + item        



    #Get Error details
    def getError(self):
        #Log error in file    
        os.system(f"{self.build_cmd} 2> \"{self.errorFile_path}\" ")
                
        #Open error loging file for reading
        self.errFile=open(f'{self.errorFile_path}', "r")

        #Get TXT file content
        self.err=self.errFile.read()

        #Close error file
        self.errFile.close()

        #delete the file after getting the eror
        os.remove(self.errorFile_path)
        
        return self.err
    


    #Validate the output file name
    def validateFileName(self,filename):
        #List of unvalid characters to check
        nonValidChr=['>','<',':','\"','/','\\','|','?','*']
        reservedNames= ("CON", "PRN", "AUX", "NUL" 
			"COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9"
			"LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9")
        #Check if the user entered the output name if not set it to defualt "Output"
        # and then check if it is a reserved name or contains an invalid chr 
        # or ends in "." or " " 
        if filename.isspace() or filename == "":
            pass
        elif (filename in reservedNames or filename.endswith((" ","."))
            or any(chr in filename for chr in nonValidChr) ):
            return True
        else:
            self.output_name=filename



    #Open Help page -> Github link
    def helpPage(self):
        os.system("start chrome https://github.com/Ziad-Elshrief/C-Cpp_ProjectBuilder ")
                 

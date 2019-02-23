import os

'''
   This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 
'''

def print_directory_contents(stringPath):
    pathList = ()
    import os                                       
    for sChild in os.listdir(stringPath):                
        sChildPath = os.path.join(stringPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            pathList.append(sChildPath)
 
print(pathList)

import os

# mydir = os.getcwd()
# mydir_tmp = mydir + "\\code"
mydir_tmp = f"{os.path.dirname(os.getcwd())}/code"
mydir_new = os.chdir(mydir_tmp) 
os.system('python main.py')
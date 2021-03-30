import os

# mydir = os.getcwd()
# mydir_tmp = mydir + "\\code"
os.system('pip install -r requirements.txt')
mydir_tmp = f"{os.getcwd()}/code"
mydir_new = os.chdir(mydir_tmp) 
os.system('python main.py')
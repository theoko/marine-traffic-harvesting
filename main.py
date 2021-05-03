import subprocess
import sys


def install_pip_and_package(package):
    # check if get-pip.py exists
    import os.path
    if not os.path.isfile("./get-pip.py"):
        subprocess.check_call(["curl", "https://bootstrap.pypa.io/get-pip.py", "-o",
                               "get-pip.py"])  # curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    # open terminal and press enter whenever 'python get-pip.py'
    # in order to continue the execution of the program
    # input('Please open your terminal window and run the following: python get-pip.py')
    subprocess.check_call([sys.executable, "get-pip.py"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
if __name__ == '__main__':
    install_pip_and_package("selenium")

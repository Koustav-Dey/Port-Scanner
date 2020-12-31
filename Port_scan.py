import pyfiglet
import socket
import sys
from time import time
import time
import threading
import port_for

class bcolors:

    WARNING = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREEN = '\033[92m'

def wait():
    print(bcolors.WARNING + "\nWaiting ", end="")
    list1 = [".", ".", ".", ".", ".", ".", ".", "."]
    for i in (list1):
        print(f"{i}", end="")
        time.sleep(1)
    print(bcolors.ENDC)


def scan_port(port):
    protocolname = 'tcp' 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # (Address family of internet, tcp connection)
    s.settimeout(5)
    conn = s.connect_ex((target,port))
    if(not conn):
       print ("Port: %s ====> service name: %s" %(port, socket.getservbyport(port, protocolname)))
    s.close()

def scan():
    global start_port,end_port
    for port in range(start_port,end_port+1):
        thread = threading.Thread(target=scan_port, args=(port,))
        thread.start()

def check_internet():
    global target

    try:
        host = socket.gethostbyname("www.google.com") 
        s = socket.create_connection((host, 80), 2)
        s.close()
        print("\nChecking Internet Connection :::")
        wait()
        print(bcolors.GREEN+"Internet is Working"+bcolors.ENDC)  
        print("\nScanning target :", target,"\nGetting data.. ")
        wait()
        scan()
        
    except Exception as e:    
        print("\nChecking Internet Connection :::")
        wait()
        print(bcolors.WARNING+"Internet is down \n"+bcolors.ENDC+"\nCheck your Internet Connection...... \n\n")
        sys.exit()


if __name__ == "__main__":
        
    start_time = time.time() 
    usage = (bcolors.WARNING +"\nSYNTAX ERROR ! :::"+ bcolors.ENDC+bcolors.GREEN + "\n\nSyntax :: -->"+ bcolors.ENDC + "\t 'python3' 'port_scanner.py' 'TARGET_START_PORT' 'TARGET_END_PORT'")
    if (len(sys.argv) != 4):
        print(usage)
        print(bcolors.WARNING +"\nTry Again !\n"+ bcolors.ENDC)
        sys.exit()
    
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    figlet_data = pyfiglet.figlet_format(
        "\nPort Scanner By Koustav")

    print(bcolors.BOLD + bcolors.WARNING +
        "\n\n========================================" + bcolors.ENDC)
    print(figlet_data)
    print(bcolors.BOLD + bcolors.WARNING +
        "========================================\n" + bcolors.ENDC)

    try:
        target = socket.gethostbyname(sys.argv[1])

    except sockket.gaierror:
        print("Name resoliution error - Address info not found!")
        sys.exit()
    
    check_internet()
    
    end_time = time.time()

    time_gape = (start_time-end_time)*-1
    get_time = "{:.2f}".format(time_gape)

print("Time elapsed : ",get_time,"secs\n")
sys.exit()     
  
  
    
   
  
import cx_Oracle

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   DARKGREY = '\033[90m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   GREENBACK = '\x1b[6;30;42m'
   WHITEBACK = '\x1b[7;30;41m'
   BACKEND = '\x1b[0m'

def hello():
    try:
        client_version = cx_Oracle.clientversion()
        print "Running with " + color.BOLD + "Oracle version v" + ".".join(str(x) for x in client_version)
        print(color.GREEN +' Hurry! It Installed Successfully :) ' + color.END +
              '\n')
    except:
        print(color.RED + ' Oops! Build Failed :( ' + color.END +
              '\n')
    print(color.YELLOW +' MAINTAINER Naresh,Surisetty <nareshskyrocket@gmail.com> ' + color.END)

if __name__ == "__main__":
    hello()
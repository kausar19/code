import cmd   #use lowercase cmd

class Myshell(cmd . Cmd):   #Cmd must be capitalized
    def do_greet(self,line):
        print("Hi, kausar")

        def do_exist(self,line):
            return True
        
Myshell().cmdloop()
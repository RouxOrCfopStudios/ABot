print("Welcome to ABot! Type help for a list of commands.")
print("Note: ABot might crash if you do something inappropriate, so please use ABot wisely.")
while True:
    user = input("> ")
    
    if user == "help":
        print("about\nhelp\nspecs\nlink(not recommended)\nendsession\ndirmk\ndirrm\ndirinfo\ninfspam(not recommended)\nnotepad")

    elif user == "about":
        print("ABot was created by RouxOrCfop Studios.\nABot beta version 1.0.1.7")

    elif user == "specs":
        print("error:in development, coming soon.")

    elif user == "link":
        while True:
            print("https://www.youtube.com/watch?v=iik25wqIuFo")

    elif user == "endsession":
        break
    
    elif user == "dirmk":
        dirname = input("enter the name of the directory:")
        print("the directory", dirname, "has been created")

    elif user == "dirrm":
        dirnamerm = input("enter the name of the direcory you want to remove:")
        if dirnamerm == dirname:
            print("the directory has been removed.")

        else:
            print("this directory does not exist.")

    elif user == "dirinfo":
        dirinfo = input("which info of which directory?:")
        if dirinfo == dirname:
            print("file name:",dirname,"\nconsumed ram:15 KB\nconsumed cpu: 4 KB\nfile type: Directory")
        else:
            print("this directory does not exist.")

    elif user == "":
        continue


    elif user == "infspam":
        while True:
            print("you can only exit this by doig alt + f4 or closing the window. Enjoy :)")

    elif user == "notepad":
        while True:
            notepad = input("")

            if notepad == "exit":
                break

    else:
        print("This is not a command. It may be a typo, or maybe the text had caps, but if you do not know the commands, type help for a list of commands.")
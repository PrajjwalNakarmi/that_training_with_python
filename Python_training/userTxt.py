def user_input():

    user_input= input("Enter something")
    text_file(user_input)


def text_file(user_input):
    file=open("sepaarateFile.txt","w")
    file.write(user_input)
    
user_input()
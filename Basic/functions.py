def sqaure(x):
    return x*x
    
#this function will only run when functions.py is excuted and not when it is called 
def main(): 
    for i in range(10):
        print(f"{i} squared is {sqaure(i)}")

#if currently I am running this file then run the main function
if __name__ == "__main__":
    main()
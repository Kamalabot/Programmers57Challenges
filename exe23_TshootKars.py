#Lets troubleshoot some cars...

"""This program starts by asking questions 
about the car trouble, and provides appropriate 
solutions. 

Later the rules / inference engines that are native to 
python will be explored

Multiple rule engines were found on the internet, starting with
NASA's CLIPS, Intellect, Pyke and Drools. Pyke seems to be a 
bit user friendly. Need to learn and implement this expert 
system...

"""

print("""Expert system will ask you series of questions 
about your car trouble, please answer with "y" or "n". """)

l1 = input("Is the car silent when you turn on the key? : ").lower()

if l1 == 'y':
    l2 = input("Are the battery terminals corroded? : ").lower()

    if l2 == 'y':
        print("Clean the terminals and try to start")
    
    else:  
        print("Replace the cables and try again")
else:
    l2 = input("Does the car make clicking noise? ").lower()

    if l2 == 'y':
        print("Relace the battery")

    else:
        l3 = input("Does the car crank up and fail to start? ").lower()

        if l3 == 'n':
            l4 = input('Does the engine start and die? ').lower()

            if l4 == 'y':
                l5 = input('Does you car have fuel injection? ').lower()

                if l5 == 'y':
                    print('Check and ensure choke is opening n closing')

                else:
                    print('Get your car to servicing')
            
        else:
            print("Check the spark plug and try strating again")


'''
Project Name: Yondu Udonta
Author: Nixson Siriphone
Due Date: 09/12/2020
Course: CS1400-003

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
'''

def main():
    '''
    Program starts here.
    '''
    try:
        # (1) replace pass with your code
        pass
    except ValueError:
        print("Enter postive integers for reavers and units.")
        return
    
   if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return
    
    # (2) replace pass with your code
    pass

if __name__ == "__main__":
    main()
    
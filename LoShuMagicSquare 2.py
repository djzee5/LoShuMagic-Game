import random #import the random to choose random numbers
import turtle
wins = 0 #Calculate the total wins
losses= 0 #calculate the total losses
runs = 0 #calculate the number of iterations
def main(): #define the main function
    global wins
    global losses
    global runs #Use the global function to access the variables outside the main def
    MainMenu()

    start_new_game = 'y'
    while start_new_game == 'y' or 'Y': #Create a while loop
         try:
            print('Current Score') #Display your current scores and runs
            print('Wins: ',wins)
            print('Losses: ', losses)
            print('Runs: ', runs)


            option = int(input('to start a new game enter 1, to pick numbers at random enter 2\n'
                                       'to quit the game enter 0 \n'
                                 'Select an option: ')) #prompt the user for an option on the Lo shu grid
            if option == 1 :
                start_game() #Display the start game definition if user selects 1
            elif option== 2:
                Random() #Display the random definition if user selects 2
            elif option == 0:
                print('Thanks for playing Lo shu Magic Square game\n'
                'come again next time!')
                break #Stop the game
            else:
                print('The input was invalid, read the option again and select carefully!')
        except ValueError: #Display an exception incase the user enter an invalid character
            print('User has entered a character, read the option again and select carefully!')

        print('\nNOTE: Exit out of the turtle graphics to continue playing')
        turtle_graphics(runs, losses, wins)



def MainMenu(): #Define the main menu
    print('This is a Lo Shu Magic Square Game!')
    print('Instructions on how to play this game:')
    print('Numbers between 1-9 needs to be arranged in a 3x3 grid square. You can only select the same number once')
    print('If the sum of each rows in the grid, the sum of each column and the sum of each diagonals all equal 15')
    print('You Win, else You Lose')
    print('.......................')
    
    print('Enter Lo Shu numbers from 1-9. \n'
          'The first 3 numbers represent the first row in the grid square. \n'
          'The next 3 represent the second row in the grid square. \n'
          'The final 3 represent the third row in the grid square.')

def start_game(): #define the start game
    global wins #Prompt the global variables
    global losses
    global runs
    try: #use the try and except function to handle exceptions
        LoShuGrid = [0,0,0,    #Create a list that accepts user input
                     0,0,0,
                     0,0,0]
        Input = []  #create an empty square bracket to hold users input
        count=0
        for i in range (1,10): #select numbers from 1-9
            num=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
            i = int(input('Enter the '+num[count]+' Lo Shu number: ')) #prompt user for the numbers to input into the grid
            if i < 1:
                print('The numbers has to be in the range of 1-9. re-enter the number!')
                return #incase user enters a number less than 1, it displays the print function

            elif i > 9:
                print('The numbers has to be in the range of 1-9. re-enter the number!')
                return #incase user enters a number less than 1, it displays the print function

            elif i in LoShuGrid:
                print('You can not enter the same number twice')
                return #incase thre user enters a number that is already stored in the grid, it restarts
            else:  #If the user enters the right integers, it goes to the next step
                Input.append(i)
                LoShuGrid = Input #replaces the L shu grid with the new input numbers
                count+=1

        print(LoShuGrid[:3])
        print(LoShuGrid[3:6])
        print(LoShuGrid[6:])
        if sum(LoShuGrid): #Call the definition of the Lo shu grid sum to test if it is correct
            print('You won! \n'
                  'This is a Lo shu Magic Square')
            wins+=1
            runs+=1

        else:
            print('You lost \n'
                  'This is not a Lo shu Magic square!')
            losses+=1
            runs+=1
    except ValueError:
        print('User has entered a character. Enter a number from 1-9 and\n'
              'restart the game!') #raise an exception if user enters a character

def Random(): #Prompt the random function
    global wins #Prompt the global variables
    global losses
    global runs
    random_nums = list(range(1,10)) #displays random numbers from 1,9
    random.shuffle(random_nums) #shuffles the random numbers that was selected
    LoShuGrid = random_nums[:] #fill the Lo shu grid with the random numbers
    print (LoShuGrid[0:3])
    print (LoShuGrid[3:6])
    print (LoShuGrid[6:10]) #displays the lo shu grid
    if sum(LoShuGrid): #test if it is correct
        print('You won! \n'
              'This is a Lo shu Magic Square')
        wins += 1
        runs += 1

    else:
        print('You lost \n'
              'This is not a Lo shu square!')
        losses += 1
        runs += 1

def sum(LoShuGrid):
    row1= LoShuGrid[0] + LoShuGrid[1] + LoShuGrid[2]
    row2 = LoShuGrid[3]   + LoShuGrid[4]    + LoShuGrid[5]
    row3 = LoShuGrid[6] + LoShuGrid[7] + LoShuGrid[8]
    col1 = LoShuGrid[0] + LoShuGrid[3] + LoShuGrid[6]
    col2 = LoShuGrid[1] + LoShuGrid[4] + LoShuGrid[7]
    col3 = LoShuGrid[2] + LoShuGrid[5] + LoShuGrid[8]
    diag1= LoShuGrid[0] + LoShuGrid[4] + LoShuGrid[8]
    diag2 = LoShuGrid[2] + LoShuGrid[4] + LoShuGrid[6]    #Calculates all the sides and diagonals of the grid
    if row1== 15 and row2 == 15 and row3 == 15 and col1== 15 and col2== 15 and col3== 15 and diag1== 15 and diag2== 15:
        return True #test if the sum equals 15
    else:
        return False



def turtle_graphics(runs, losses, wins):
    turtle.TurtleScreen._RUNNING=True   #So we do not get the termination error
    turtle.title('Lo shu magic square game')
    turtle.bgcolor('black')
    turtle.speed(1)
    turtle.shape('square')
    turtle.color('white')
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0,250)
    turtle.write('Total runs : {} Total losses : {} Total wins : {}'.format(runs, losses, wins), align='center', font=('candara', 25, 'bold'))
    turtle.exitonclick()


    
main() #call the program








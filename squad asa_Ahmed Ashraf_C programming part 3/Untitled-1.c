#include <stdio.h>
#include <stdlib.h>

int main()
{
    int secretNumber = 4;
    int playerGuess;
    int gameMode;
    int limitedTrials = 5;

    printf("Welcome to the guessing game\nPlease Choose your mode\n1.Infinite \t 2.Limited(only 5 guesses)\n");
    scanf("%d",&gameMode);

    switch(gameMode){
        case 1:
            printf("Enter the number: ");
            scanf("%d",&playerGuess);
            while(playerGuess!=4){
                printf("Incorrect guess try again. Enter the number: ");
                scanf("%d",&playerGuess);
            }
            printf("Congrats you won!");
            break;

        case 2:
            printf("You have %d trials left enter the number: ",limitedTrials);
            scanf("%d",&playerGuess);
            while(playerGuess!=4 && limitedTrials!=1){
                limitedTrials--;
                printf("Incorrect guess try again. You have %d trials left enter the number: ",limitedTrials);
                scanf("%d",&playerGuess);

            }
            if(limitedTrials==1){
                printf("You lost!!");
            }
            else{
            printf("Congrats you won!");
            }
            break;
    }
    return 0;
}

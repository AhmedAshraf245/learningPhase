#include <stdio.h>
#include <stdlib.h>

int main() {
    float firstNumber;
    float secondNumber;
    int op;
    printf("Enter first number: ");
    scanf("%f",&firstNumber);
    printf("Enter second number: ");
    scanf("%f",&secondNumber);

    printf("Choose operator:\n");
    printf(" 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division \n");
    scanf("%d", &op);
    switch(op){
    case 1 :
         printf("result = %f" , firstNumber + secondNumber);
         break;
    case 2 :
        printf("result = %f" , firstNumber - secondNumber);
        break;
    case 3 :
        printf("result = %f" , firstNumber * secondNumber);
        break;
    case 4 :
        printf("result = %f" , firstNumber / secondNumber);
        break;
    default : printf("Invalid operation");
    }


}


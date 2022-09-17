#include <stdio.h>
#include <stdlib.h>

int main() {
    float firstNumber;
    float secondNumber;
    float thirdNumber;

    printf("Enter the first number: ");
    scanf("%f",&firstNumber);
    printf("Enter the second number: ");
    scanf("%f",&secondNumber);
    printf("Enter the third number: ");
    scanf("%f",&thirdNumber);

    float sum = firstNumber + secondNumber + thirdNumber;
    float avg = sum / 3;

    printf("sum = %f \t avg = %f",sum,avg);
}

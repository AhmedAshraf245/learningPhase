#include <stdio.h>
#include <stdlib.h>

int main() {
    int firstNumber;
    int secondNumber;
    int thirdNumber;

    printf("Enter the first number: ");
    scanf("%d",&firstNumber);
    printf("Enter the second number: ");
    scanf("%d",&secondNumber);
    printf("Enter the third number: ");
    scanf("%d",&thirdNumber);

    int sum = firstNumber + secondNumber + thirdNumber;
    int avg = sum / 3;

    printf("sum = %d \t avg = %d",sum,avg);
}
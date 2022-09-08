#include <stdio.h>
#include <stdlib.h>

int main() {
    char color[20];
    char song[20];
    char celebrityFirstName[20];
    char celebrityLastName[20];
    printf("Enter color: ");
    scanf("%s", color);
    printf("Enter song: ");
    scanf("%s", song);
    printf("Enter celebrity's first name : ");
    scanf("%s", celebrityFirstName);
    printf("Enter celebrity's last name : ");
    scanf("%s", celebrityLastName);

    printf("Roses are %s\n",color);
    printf("%s are blue\n",song);
    printf("I love %s %s\n", celebrityFirstName ,celebrityLastName);

}
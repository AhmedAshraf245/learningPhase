#include <stdio.h>
#include <stdlib.h>

int main() {
    int height;
    printf("Enter pyramid height (a value between 2 & 5): ");
    scanf("%d",&height);
    while(height < 2 || height >5){
        printf("Enter pyramid height (a value between 2 & 5): ");
        scanf("%d",&height);
        if(height > 2 && height < 5) break;
    }

    char height2[2][4] = {" *","***"};

    char height3[3][6] = {"  *"," ***","*****"};

    char height4[4][8] = {"   *","  ***"," *****","*******"};

    char height5[5][10] = {"    *","   ***","  *****"," *******","*********"};

    printf("Output pyramid is:\n");
    switch(height){
    case 2 :
        printf("%s\n%s",height2[0],height2[1]);
        break;
    case 3 :
        printf("%s \n%s \n%s",height3[0],height3[1],height3[2]);
        break;
    case 4 :
        printf("%s\n%s\n%s\n%s",height4[0],height4[1],height4[2],height4[3]);
        break;
    case 5 :
        printf("%s\n%s\n%s\n%s\n%s",height5[0],height5[1],height5[2],height5[3],height5[4]);
        break;
    }

}

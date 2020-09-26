#include<stdio.h>

#include<string.h>

void maxim(int array[]);
int main()

{
    int array[10] = {1,2,3,4,7,8,7,9,9,9};
    int max = array[0],indexs[9];
    for (int i = 0; i < 10; i++)
    {
        if(max<array[i])
        {
            max =array[i];
            indexs =i;

        }
    }
    maxim(array);
    // printf("%i index at %i",max,index);
}

void maxim(int arr[]) {
    int max = arr[0];
    // var maxIndices = [];
    for (int i = 0; i < 10; i++) {
        
        } else if (arr[i] > max) {
            maxIndices = [i];
            max = arr[i];
        }
    }
    return maxIndices;
 }
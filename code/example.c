#include <stdlib.h>

main(){
    int i, n;
    int* array;
    n = 10000000;
    array = malloc(n * sizeof(int));
    for (i = 0 ; i < n ; i++){
        array[i] = i * i;
    }
}

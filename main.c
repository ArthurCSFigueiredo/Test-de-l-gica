#include <stdio.h>

int main()
{
    int indice=13, soma=0, contador=0;
    while(contador<indice){
        contador++;
        soma=soma+contador;
        printf("Soma: %d \n", soma);
    }
    return 0;
}
// resultado:
    // Soma: 1 
    // Soma: 3 
    // Soma: 6 
    // Soma: 10 
    // Soma: 15 
    // Soma: 21 
    // Soma: 28 
    // Soma: 36 
    // Soma: 45 
    // Soma: 55 
    // Soma: 66 
    // Soma: 78 
    // Soma: 91 
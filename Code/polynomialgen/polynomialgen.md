# polynomial gen

This application is written in c and creates 10 random quadratic formulas. The code can be easily modified to create higher or lesser degree polynomials with more or less terms. 

## code

```
#include <stdio.h>
#include <stdlib.h>

int main()
{
   time_t t;
   srand((unsigned)time(&t));
   for(int i = 0; i < 10; ++i)
   {
      int a = rand() %10;
      int b = rand() %10;
      int c = rand() %10;
      printf("%ix^2 + %ix + %i\n",a,b,c);
   }
   return 0;
}
```

## compiling

This program can be compiled with the following command:
`gcc -o polynomialgen polynomialgen.c` provided that you are in the directory with a file called polynomialgen.c which contains the code listed above.

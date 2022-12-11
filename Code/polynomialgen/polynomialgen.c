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

#include<stdio.h> 
#include<stdlib.h>
#include <time.h>
 
int main()
{
  int n,k,i,j;
  int p[1000]={0};
  int result[1000]={0};
  
  clock_t before,after;    
  k=0;
  n=2;
  before = clock();
  while (k<1000)
  {
      i=0;
      while (i<k && n%p[i]!=0)
      {
          i=i+1;
      }
  if (i==k)
  {
     p[k]=n;
     k++;
     result[k-1]=n;
  }
  n++;
      
   }
 
  after = clock();
   
for (j=0;j<1000;j++)
printf("%d  ",result[j]);    
printf("\nseconds:%lf\n",(after-before)/(double)(CLOCKS_PER_SEC));
 
return 0;
}
 
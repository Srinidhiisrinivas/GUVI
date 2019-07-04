#include<stdio.h>
#include<conio.h>
int main()
{
int aa,bb,cc;
printf("Enter the three numbers aa and bb and cc:");
scanf("%d%d%d",&aa,&bb,&cc);
if((aa>bb)&&(aa>cc))
 printf("%d",aa);
 {
  if((bb>aa)&&(bb>cc))
   printf("%d",bb);
  else
     printf("%d",cc);
  }
return 0;
}

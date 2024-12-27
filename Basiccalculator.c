#include <stdio.h>
int main()
{
  int a,b;
  char operator;
  printf("Enter a and b values : ");
  scanf("%d %d",&a,&b);
  printf("Enter an operator (+, -, *, /, %):\n");
  scanf(" %c",&operator);
  switch (operator)
  {
    case '+':
    {
      printf("Addtion of two numbers %d and %d is %d\n",a,b,(a + b));
      break;
    }
    case '-':
    {
      printf("Subtraction of two numbers %d and %d is %d\n",a,b,(a - b));
      break;
    }
    case '*':
    {
      printf("Multiplication of two numbers %d and %d is %d\n",a,b,(a * b));
      break;
    }
    case '/':
    {
      printf("Division of two numbers %d and %d is %d\n",a,b,(a / b));
      break;
    }
    case '%':
    {
      printf("Modulo Division of two numbers %d and %d is %d\n",a,b,(a % b));
      break;
    }
    default:
    {
      printf("No operator is available");
      break;
    }
  }
  return 0;
}
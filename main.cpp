#include <iostream>

/* A simple program that outputs a different message depending on the 
 * value of x. Normally, it impossible to change 'x' without recompiling.
 * This is were our little python script comes in. :)*/
int main() {
  int x = 0;

  if (x > 5) {
    std::cout << "X is Greater than 5.";
  }
  else {
    std::cout << "X is lower than 5.";
  }

  return 0;
}

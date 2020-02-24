// person_test.cxx -- testing the Person class

#include <iostream>
#include "person.h"

int main(int argc, char *argv[])
{
  Person p("Max Student");
  std::cout << "Name p: " << p.get_name() << std::endl;
  p.set_name("Maria Student");
  std::cout << "Name p: " << p.get_name() << std::endl;

  Person p2(p);
  std::cout << "Name p2: " << p2.get_name() << std::endl;

  return 0;
}

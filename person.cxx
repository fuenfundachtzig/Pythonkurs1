// person.cxx -- a C++ class

#include <iostream>
#include "person.h"

Person::Person(const char *name)
{
  name_ = std::string(name);
}

Person::Person(const Person &anotherOne)
{
  name_ = std::string(anotherOne.get_name());
}

Person::~Person()
{
  std::cout << "Person::~Person() called" << std::endl;
}

const std::string & Person::get_name(void) const
{
  return name_;
}

void Person::set_name(const char *newname)
{
  name_ = std::string(newname);
}

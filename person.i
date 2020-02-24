%module person
%include "std_string.i"

%{
#include "person.h"
%}

class Person {
 public:
  Person(const char *name);
  Person(const Person &anotherOne);
  virtual ~Person();

  const std::string &get_name(void) const;
  void set_name(const char *newname);

 private:
  std::string name_;
};

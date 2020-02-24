// person.h -- a C++ class

#ifndef _PERSON_H_
#define _PERSON_H_

#include <string>

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

#endif /* _PERSON_H_ */

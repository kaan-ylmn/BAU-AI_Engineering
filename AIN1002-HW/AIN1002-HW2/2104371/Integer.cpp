#include "Integer.h"

Integer::Integer(int year)
    : hold{year} {}
    

int Integer::toInteger() const{
    return this->hold;
}

Number *Integer::operator++(int num){
    this->hold = this->hold + 1;
    Number *temp = new Integer(hold);
    return temp;
}


Number *Integer::operator--(int){
    this->hold = this->hold - 1;
    Number *temp = new Integer(hold);
    return temp;
}
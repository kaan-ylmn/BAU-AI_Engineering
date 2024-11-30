#include "PositiveInteger.h"

PositiveInteger::PositiveInteger(int hold)
    :hold{hold} {}


Number *PositiveInteger::operator--(int){
    if(this->hold > 0){
        this->hold = this->hold - 1;
        Number *temp = new PositiveInteger(hold);
        return temp;
    }
    Number *temp = new PositiveInteger(hold);
    return temp;
}


Number *PositiveInteger::operator++(int){
    this->hold = this->hold + 1;
    Number *temp = new PositiveInteger(hold);
    return temp;
}

int PositiveInteger::toInteger() const{
    return hold;
}

#include "Bool.h"

Bool::Bool(int hold)
    :hold(hold) {}

int Bool::toInteger() const{
    return hold;
}


Number *Bool::operator++(int){
    if(this->hold == 1){
        this->hold = 0;
        Number *temp = new Bool(hold);
        return temp;
    }else{
        this->hold = 1;
        Number *temp = new Bool(hold);
        return temp;
    }
}



Number *Bool::operator--(int){
    if(this->hold == 0){
        this->hold = 1;
        Number *temp = new Bool(hold);
        return temp;
    }else{
        this->hold = 0;
        Number *temp = new Bool(hold);
        return temp;
    }

}
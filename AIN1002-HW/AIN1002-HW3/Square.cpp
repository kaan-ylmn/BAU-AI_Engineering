#include "Square.h"

Square::Square(int x_cord,int y_cord,double length)
    :PlanarShape(x_cord,y_cord),length{length}{}

double Square::circumference() {return (4.0 * this->length);}

double Square::area(){return (this->length * this->length);}


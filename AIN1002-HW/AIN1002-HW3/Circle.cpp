#include "Circle.h"

Circle::Circle(int x_cord, int y_cord,double radius)
    :PlanarShape(x_cord,y_cord),radius{radius}{}

double Circle::circumference(){return (2 * pi * this->radius);}

double Circle::area(){return (pi * this->radius * this->radius);}



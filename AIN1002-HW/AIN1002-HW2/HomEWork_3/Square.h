#ifndef SQUARE_H
#define SQUARE_H
#include "PlanarShape.h"

class Square: public PlanarShape{
private:
    int x_cord;
    int y_cord;
    double length;
public:
    Square(int x_cord = 0,int y_cord = 0,double length = 1.0);
    virtual double circumference() override;
    virtual double area() override;
};

#endif // SQUARE_H
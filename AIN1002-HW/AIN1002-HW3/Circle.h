#ifndef CIRCLE_H
#define CIRCLE_H
#include "PlanarShape.h"

class Circle: public PlanarShape{
private:
    int x_cord;
    int y_cord;
    double radius;
    double pi = 3.14; 
public:
    Circle(int x_cord = 0, int y_cord = 0, double radius = 1.0);
    virtual double circumference() override;
    virtual double area() override;
};

#endif // CIRCLE_H

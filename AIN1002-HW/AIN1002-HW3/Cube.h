#ifndef CUBE_H
#define CUBE_H
#include "Square.h"
#include "VolumetricShape.h"

class Cube: public VolumetricShape,public Square{
private:
    int x_cord;
    int y_cord;
    int z_cord;
    double length;
public:
    Cube(int x_cord = 0, int y_cord = 0, int z_cord = 0, double length = 1.0);
    virtual double area() override;
    virtual double volume() override;
};

#endif // CUBE_H

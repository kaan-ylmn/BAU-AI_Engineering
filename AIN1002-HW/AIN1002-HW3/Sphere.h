#ifndef SPHERE_H
#define SPHERE_H
#include "Circle.h"
#include "VolumetricShape.h"

class Sphere: public VolumetricShape, public Circle{
private:
    int x_cord;
    int y_cord;
    int z_cord;
    double radius;
public:
    Sphere(int x_cord = 0, int y_cord = 0, int z_cord = 0, double radius = 1.0);
    virtual double area() override;
    virtual double volume() override;
};

#endif // SPHERE_H


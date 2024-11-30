#ifndef VOLUMETRICSHAPE_H
#define VOLUMETRICSHAPE_H
#include "Shape.h"

class VolumetricShape: public Shape{
private:    
    int x_cord;
    int y_cord;
    int z_cord;
public:
    VolumetricShape(int x_cord = 0, int y_cord = 0, int z_cord = 0);
    virtual double area() override;
    virtual double volume() = 0;
    virtual ~VolumetricShape() = default;
};

#endif // VOLUMETRICSHAPE_H

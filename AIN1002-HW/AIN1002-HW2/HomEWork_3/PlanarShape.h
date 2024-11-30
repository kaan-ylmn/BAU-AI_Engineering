#ifndef PLANARSHAPE_H
#define PLANARSHAPE_H
#include "Shape.h"

class PlanarShape: public Shape{
private:
    int x_cord;
    int y_cord;
public:
    PlanarShape(int x_cord = 0, int y_cord = 0);
    virtual double area() override;
    virtual double circumference() = 0;
    virtual ~PlanarShape() = default;
};

#endif // PLANARSHAPE_H

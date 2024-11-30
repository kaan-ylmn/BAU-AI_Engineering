#include "VolumetricShape.h"

VolumetricShape::VolumetricShape(int x_cord, int y_cord, int z_cord)
    :Shape(x_cord,y_cord),z_cord{z_cord} {}

double VolumetricShape::area() {}


#include "Cube.h"

Cube::Cube(int x_cord, int y_cord,int z_cord, double length)
    :VolumetricShape(x_cord,y_cord,z_cord), Square(x_cord,y_cord,length), length{length} {}

double Cube::area(){
    return (6 * Square::area());
}

double Cube::volume(){
    return (this->length * Square::area());
}



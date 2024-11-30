#include "Sphere.h"

Sphere::Sphere(int x_cord, int y_cord, int z_cord, double radius)
    : Circle(x_cord,y_cord,radius), z_cord{z_cord}, radius{radius} {}


double Sphere::area(){
    return (4 * Circle::area());
}

double Sphere::volume(){
    return (area() * this->radius) / 3;
}



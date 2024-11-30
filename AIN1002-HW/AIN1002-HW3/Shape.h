#ifndef SHAPE_H
#define SHAPE_H

class Shape{
private:
    int x_cord;
    int y_cord;
public:
    Shape(int x_cord = 0, int y_cord = 0);
    virtual double area() = 0;
    virtual ~Shape() = default;
};

#endif // SHAPE_H
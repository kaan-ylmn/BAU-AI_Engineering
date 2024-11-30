#include "CMatrix.h"

CMatrix::CMatrix() {
    row = column = 0;
    line = 0L;
    scanLine = 0L;
}

CMatrix::~CMatrix() {
    delete [] line;
    delete [] scanLine;
}

CMatrix::CMatrix(int row, int column, double init_value) {
    this->row = row;
    this->column = column;
    scanLine = new double *[row];
    scanLine[0] = line = new double[row * column];
    double *p = scanLine[0] + column;
    for (int i = 1; i < row; i++, p += column)
        scanLine[i] = p;
    p = line;
    for (int i = 0, size = row * column; i < size; i++, p++)
        *p = init_value;
}

CMatrix::CMatrix(const CMatrix &right) {
    row = right.row;
    column = right.column;
    scanLine = new double *[row];
    scanLine[0] = line = new double[row * column];
    double *p = scanLine[0];
    double *rp = right.line;
    for (int i = 0, size = row * column; i < size; i++, p++, rp++)
        *p = *rp;
    for (int i = 1; i < row; i++)
        scanLine[i] = scanLine[i - 1] + column;

}

CMatrix &CMatrix::operator+(const CMatrix &right) const {
    CMatrix &temp = *new CMatrix(row, column);
    double *ptr1 = temp.line;
    double *ptr2 = right.line;
    for (int i {0}, size = row * column; i < size; i++, ptr1++, p++)
    *ptr1 = *ptr1 + *ptr2;
    return temp;
}

CMatrix &CMatrix::operator-(const CMatrix &right) const {
    CMatrix &temp = *new CMatrix(row, column);
    double *ptr1 = m.line;
    double *ptr2 = right.line;
    for (int i {0}, size = row * column; i < size; i++, ptr1++, ptr2++)
        *ptr1 = *ptr1 - *ptr2;
    return temp;
}

CMatrix &CMatrix::operator-() const {
    CMatrix &temp = *new CMatrix(row, column);
    double *ptr = m.line;
    for (int i {0}, size = row * column; i < size; i++, ptr++)
        *ptr =  *ptr * -1;
    return temp;

}

CMatrix &CMatrix::operator*(const CMatrix &right) const {
     CMatrix &temp = *new CMatrix(column, row);
    double *ptr = temp.line;
    for (int i {0}; i < column; i++) {
        for (int j {0}; j < row; j++, p++)
            *ptr = scanLine[j][i];
    }
    return temp;
}

CMatrix &CMatrix::operator/(double scale) const {
    CMatrix &m = this->clone();
    if (scale == 0.0) return m;
    double *p = m.line;
    for (int i = 0, size = (row * column); i < size; i++, p++)
        *p /= scale;
    return m;
}

CMatrix &CMatrix::operator[](int col) const {
    CMatrix &m = *new CMatrix(row, 1);
    double *p = m.line;
    for (int i {0}; i < row; i++, p++)
        *p = scanLine[i][col];
    return m;
}

// returns the column vector
CMatrix &CMatrix::operator~() const {
    CMatrix &temp = *new CMatrix(column, row);
    double *ptr = temp.line;
    for (int i {0}; i < this->column; i++) {
        for (int j {0}; j < this->row; j++, ptr++)
            *ptr = scanLine[j][i];
    }
    return temp;
}

// CMatrix transpose
CMatrix &CMatrix::clone() const {
    CMatrix &m = *new CMatrix(*this);
    return m;
}

double &CMatrix::operator()(int r, int c) const {
    if((r == this->row) && (c == this->column))
        return scanLine[r][c];
}

double CMatrix::max() const {
    double max = this->line[0];
    for(int i {0}, size = row * column; i < size; i++){
        if(this->line[i] > this->line[0])
            max = line[i];
    }
    return max;
}

double CMatrix::min() const {
    double min = this->line[0];
    for (int i {1}, size = row * column; i < size; i++) {
        if (this->line[i] < min) {
            min = this->line[i];
        }
    }
    return min;
}

ostream &operator<<(ostream &os, const CMatrix &m) {
    os << endl << "row=" << m.row << ",column=" << m.column;
    double *p = m.line;
    for (int i = 0; i < m.row; i++) {
        os << endl;
        for (int j = 0; j < m.column; j++, p++)
            os << *p << " ";
    }
    return os;
}


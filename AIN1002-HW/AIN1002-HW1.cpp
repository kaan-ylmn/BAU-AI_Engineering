#include <iostream>

using namespace std;

int is_equal2(int sum1){
    int sum2;
    for(int j{1}; j < sum1; j++){
        if(sum1 % j == 0){
            sum2 += j;                   
        }
    }
    return sum2;
} 

void amicable_numbers(int num1,int num2){
    int number = num1;
    int sum1 = 0;
    int sum2;
    
    for(int i{number}; i < num2; i++){ 
        for(int j{1}; j < i; j++){
            if(i % j == 0){
                sum1 += j;                   
            }
        }
        cout << "";
        sum2 = is_equal2(sum1);
        if(sum2 == i){
            cout << "number1: " << sum2 << " and number2: " << sum1 << " are amicable numbers" <<endl;
        }
        sum1 = 0;
    }
}

int main() {
    
    amicable_numbers(1100,1300);
    
    return 0;
}

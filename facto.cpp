#include<iostream>
using namespace std;
int facto(int n)
{
    if(n==0 || n==1)
    {
        return 1;
    }
    else
    {
        return (n*facto(n-1));
    }
}

int main()
{
    int num;
    cout <<"Enter a Number : ";
    cin>>num;
    int result = facto(num);
    cout<<"Factorial of "<<num<<" = "<<result;
    return 0;
}
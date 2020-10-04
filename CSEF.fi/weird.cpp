///problem set https://cses.fi/problemset/task/1068

#include<iostream>
using namespace std;
int main()
{
    long long  num;
    cin>>num;
    while(num<1 || num >1000000)
    {
         cin>>num;
    }
    cout<<num<<" ";
    while(num>1)
    {
        if (num%2==0)
        {
            num = num/2;
            if(num)
            cout<<num<<" ";
        }
        else
        {
            num= num*3+1;
            cout<<num<<" ";
        }
        
    }

}
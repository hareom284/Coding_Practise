#include<iostream>
using namespace std;
int main()
{
    int T,output=0;
    cin>>T;
    while(T>0)
    {
         
         output+=T %10; 
         T =T/10;
        
         
    }
    T = output;
    output = 0;
    while(T>0)
    {
         
         output+=T %10; 
         T =T/10;
         
    }
    if(output<10)
    {
    cout<<output;
    }
}
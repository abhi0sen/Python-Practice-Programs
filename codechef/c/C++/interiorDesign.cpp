#include <iostream>
using namespace std;
int main(){
int T, X1, X2, Y1, Y2;

cin>>T;

for(int i=0; i<T; i++){
    cin>>X1>>Y1>>X2>>Y2;
    if((X1+Y1)<(X2+Y2)){
        cout<<(X1+Y1)<<endl;
    }
    else{
        cout<<(X2+Y2)<<endl;
    }
}
}
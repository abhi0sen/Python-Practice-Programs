#include <iostream>
using namespace std;
int main(){
int T, X, P, Q;

cin>>T;

for(int i=0; i<T; i++){
    cin>>X>>P>>Q;
    
    cout<<X*(P-Q)<<endl;
}
}
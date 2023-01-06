#include<iostream>
using namespace std;

int main(){
    int a1[5];
    int a2[5] = {7,10,3,4,5};

    cout<<"First element of the array a2 is: "<<a2[0]<<endl;


    //version -1 
    for(int i=0;i<sizeof(a2)/sizeof(*a2);i++){
        cout<<"The content of the array is :" <<a2[i]<<endl;
    }

    // version -2
    for(int& items:a2){
        cout<<"The conten in v2 is : "<<items<<endl;
    }


}
#include<iostream>
#include<vector>

using namespace std;

int main(){
    vector <int> v1;
    vector <int> v2(5,1);

    for(int i=0; i<v2.size();i++){
        cout<<"The content of the vector v2 :"<<v2[i]<<endl;
    }
}
#include<iostream>
using namespace std

int[] prodExceptSelf(nums[]){
    int res[nums.size()];
    int prefix =1;
    for(int i=0;i<nums.size();i++){
        res[i] = prefix;
        prefix *= nums[i];
    }
    int postfix=1;
    for(int i=0;i<nums.size();i--){
        res[i] *= prefix;
        prefix *= nums[i];
    }
    return res;


};

int main(){
    int nums[]={1,2,3,4}
    prodExcept
}
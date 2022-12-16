#include<iostream>
#include<vector>
using namespace std;



int pivotIndex(vector<int>& nums) {  //[1,7,3,6,5,6]
        int leftsum=0;
        int rightsum=0;
        
        for(int items:nums){
            rightsum+=items;     //R=28 , L=0
        }
        
        for(int i=0;i<nums.size();++i){
            rightsum -= nums[i];        //i=0 , R=27 , L=0
            
            if(leftsum==rightsum){
                return i;
            }
            leftsum +=nums[i];
            
        }
        return -1;
    }
int main()
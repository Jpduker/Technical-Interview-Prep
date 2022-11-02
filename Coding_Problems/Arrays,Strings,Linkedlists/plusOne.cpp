#include<iostream>
#include <bits/stdc++.h>
#include<vector>

using namespace std;


class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
         for(int i = digits.size()-1; i>=0; i--){
                    if(digits[i]<9){
                    digits[i]++;
                    return digits;
                    }
                    else
                            digits[i] = 0;
                    
            }
            digits.push_back(0);
            digits[0] = 1;
            return digits;
        
    }
};
int main(){
    Solution obj;
    vector<int> nums;
    nums.push_back(9);
    nums.push_back(9);
    nums.push_back(9);
    obj.plusOne(nums);
    for(int i=0;i<nums.size();i++){
        cout<<nums[i];
    }
    return 0;
}


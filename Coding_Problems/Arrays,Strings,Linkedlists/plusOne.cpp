class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> result;
        int len = digits.size();
        for(int i=0;i<len;i++){
            result[i]=digits[i];
        }
        result[len]+=1;
        
        return result;
        
    }
};
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int Inf = 9999999999;
        int MinSofar = Inf ;
        
        for(int i=0; i<prices.size(); i++){
            if (prices[i] < MinSofar){
                MinSofar = prices[i];
            }
            else{
                maxProfit = max(maxProfit, prices[i] - MinSofar);
            }
        }
        return maxProfit;
        
        
        
    }
};
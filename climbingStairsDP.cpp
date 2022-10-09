// Top Down Approach

#include <iostream>
#include <unordered_map>
using namespace std;

int dp(int i)
{
    unordered_map<int, int> hash;
    // base cases
    if (i <= 2)
    {
        return i;
    }
    if (hash.find(i) == hash.end())
    {
        hash.insert({i, dp(i - 1) + dp(i - 2)});
    }
    return hash.at(i);
}

int climbingStairs(int n)
{
    return dp(n);
}

int main()
{
    cout << climbingStairs(5);
}
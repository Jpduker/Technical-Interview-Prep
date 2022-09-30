#include <iostream>
using namespace std;

bool palinDromeCheck(string s)
{
    int i = 0;
    int j = s.size() - 1;

    while (i < j)
    {
        if (s[i] != s[j])
        {
            return false;
        }
        i++;
        j--;
    }

    return true;
}

int main()
{
    bool res = palinDromeCheck("racecar");
    cout << res;
}

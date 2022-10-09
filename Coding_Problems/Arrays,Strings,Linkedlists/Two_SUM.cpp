bool twoSum()
{
    int nums = new int[]{1, 2, 3, 4, 5, 6, 7, 8};

    int target = 8;
    int i = 0;
    int j = nums.size() - 1;

    while (i < j)

        if (nums[i] + nums[j] == target)
        {
            return true;
        }
    if (nums[i] + nums[j] > target)
    {
        j--;
    }
    if (nums[i] + nums[j] < target)
    {
        i++;
    }
}
return false;
}

int main()
{

    twoSum();
}
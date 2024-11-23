public class Solution 
{
    public int RemoveDuplicates(int[] nums) 
    {
        int i = 0;
        if (nums.Length == 0)
        {
            return 0;
        }
        for (int x = 0; x < nums.Length; x++)
        {
            if(nums[i] != nums[x])
            {
                nums[++i] = nums[x];
            }
        }

        return i + 1;
    }

}
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [-1]
# 输出：-1
#  
# 
#  示例 5： 
# 
#  
# 输入：nums = [-100000]
# 输出：-100000
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  
# 
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。 
#  Related Topics 数组 分治 动态规划 👍 3593 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:      # 可视为DP空间优化
        maxsum = cumsum = - 100000
        for num in nums:
            cumsum = max(cumsum + num, num)     # 截止num的最前部分和(考虑num即使num可能为负, 但可能不从首端开始)
            maxsum = max(maxsum, cumsum)        # 维护最大的截止num的部分和
        return maxsum

# leetcode submit region end(Prohibit modification and deletion)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = - float("inf")
        dp = [0] * (len(nums) + 1)
        # i+1(计数): 从nums[i]开始(含)向前计算的最大子序和
        for i in range(len(nums)):
            dp[i + 1] = nums[i] + (dp[i] if dp[i] >= 0 else 0)
            ans = max(ans, dp[i + 1])
        return ans

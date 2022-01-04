# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用一次。 
# 
#  注意：解集不能包含重复的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ] 
# 
#  示例 2: 
# 
#  
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
#  Related Topics 数组 回溯 👍 670 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start=0, cumsum=0):
            if cumsum == target:
                container.append(sublist[:])
                return
            for idx in range(start, length):
                if idx > start and candidates[idx] == candidates[idx - 1]:
                    continue
                temp = candidates[idx]
                if cumsum + temp <= target:
                    sublist.append(temp)
                    backtrack(idx + 1, cumsum + temp)
                    sublist.pop()

        container = []
        sublist = []
        candidates.sort()
        length = len(candidates)
        backtrack()
        return container

# leetcode submit region end(Prohibit modification and deletion)

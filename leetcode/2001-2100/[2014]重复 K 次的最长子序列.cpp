//给你一个长度为 n 的字符串 s ，和一个整数 k 。请你找出字符串 s 中 重复 k 次的 最长子序列 。 
//
// 子序列 是由其他字符串删除某些（或不删除）字符派生而来的一个字符串。 
//
// 如果 seq * k 是 s 的一个子序列，其中 seq * k 表示一个由 seq 串联 k 次构造的字符串，那么就称 seq 是字符串 s 中一个 重
//复 k 次 的子序列。 
//
// 
// 举个例子，"bba" 是字符串 "bababcba" 中的一个重复 2 次的子序列，因为字符串 "bbabba" 是由 "bba" 串联 2 次构造的，而
// "bbabba" 是字符串 "bababcba" 的一个子序列。 
// 
//
// 返回字符串 s 中 重复 k 次的最长子序列 。如果存在多个满足的子序列，则返回 字典序最大 的那个。如果不存在这样的子序列，返回一个 空 字符串。 
//
// 
//
// 示例 1： 
//
// 
//
// 
//输入：s = "letsleetcode", k = 2
//输出："let"
//解释：存在两个最长子序列重复 2 次：let" 和 "ete" 。
//"let" 是其中字典序最大的一个。
// 
//
// 示例 2： 
//
// 
//输入：s = "bb", k = 2
//输出："b"
//解释：重复 2 次的最长子序列是 "b" 。
// 
//
// 示例 3： 
//
// 
//输入：s = "ab", k = 2
//输出：""
//解释：不存在重复 2 次的最长子序列。返回空字符串。
// 
//
// 示例 4： 
//
// 
//输入：s = "bbabbabbbbabaababab", k = 3
//输出："bbbb"
//解释：在 "bbabbabbbbabaababab" 中重复 3 次的最长子序列是 "bbbb" 。
// 
//
// 
//
// 提示： 
//
// 
// n == s.length 
// 2 <= k <= 2000 
// 2 <= n < k * 8 
// s 由小写英文字母组成 
// 
// Related Topics 贪心 字符串 回溯 计数 枚举 👍 15 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    string target;
    int k;

    string longestSubsequenceRepeatedK(string s, int k) {   // BFS(题目描述疑有误,大于等于k次均可)
        target = s;
        this->k = k;

        string ans;
        queue<string> Q;
        vector<char> list;
        vector<int> counter(26);
        for (char letter : s) {
            counter[letter - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            if (counter[i] >= k) {
                list.push_back((char) (i + 'a'));
            }
        }
        if (list.empty()) {
            return ans;
        }

        for (char letter: list) {
            Q.push(string(1, letter));
        }
        ans += list[list.size() - 1];
        while (!Q.empty()) {
            int size = (int) Q.size();
            for (int i = 0; i < size; i++) {
                string substr = Q.front();
                Q.pop();
                for (char letter: list) {
                    string temp = substr + letter;
                    if (check(temp)) {
                        Q.push(temp);
                        if ((temp.length() > ans.length() ||
                             temp > ans)) {
                            ans = temp;
                        }
                    }
                }
            }
        }

        return ans;
    }

    bool check(string substr) { // 双指针
        int idx = 0, count = 0;
        for (char letter : target) {
            if (letter == substr[idx]) {
                idx++;
                if (idx == substr.length()) {
                    count++;
                    if (count == k) {
                        return true;
                    }
                    idx = 0;
                }
            }
        }
        return false;
    }
};

//leetcode submit region end(Prohibit modification and deletion)

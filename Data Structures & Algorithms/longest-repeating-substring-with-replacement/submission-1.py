class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            
            # Track the highest frequency of any single character seen in the current window
            max_freq = max(max_freq, count[char])
            
            # If the number of characters to change exceeds k, shrink from the left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len
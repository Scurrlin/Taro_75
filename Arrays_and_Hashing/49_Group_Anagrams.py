from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            sortedWord = tuple(sorted(word))
            group[sortedWord].append(word)
        return list(group.values())

# Time Complexity: O(n * k log k) – The primary cost comes from processing each of the n words in the input list. For every single word, we must sort its characters to create a unique key. If the maximum length of a word is k, sorting it takes O(k log k) time. Since this sorting operation is performed for all n words, the total time complexity is the product of the number of words and the cost of sorting each one. This results in a total runtime of O(n * k log k).

# Space Complexity: O(N * K) – The core of this approach is creating a collection of 'boxes' to group the anagrams, which corresponds to an auxiliary hash map or dictionary. In the worst-case scenario, where no words are anagrams of each other, this map will store N unique keys, one for each of the N input words. The values associated with these keys are lists containing the original words, and the space required to store all these words is equivalent to the total number of characters in the input list. Therefore, the space complexity is O(N * K), where N is the number of words and K is the maximum length of a word.
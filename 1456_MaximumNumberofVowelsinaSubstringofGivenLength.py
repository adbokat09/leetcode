class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        vowel_count = sum(1 for letter in s[:k] if letter in vowels)
        max_vowel_count = vowel_count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                vowel_count -= 1
            if s[i] in vowels:
                vowel_count += 1
            max_vowel_count = max(max_vowel_count, vowel_count)

        return max_vowel_count

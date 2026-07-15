class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #We use a dictionary to track the frequency of a number in nums:  {num: frequency}.
        freq_count = {} #For example: nums = [1,2,2,2] => freq_count = {1:1, 2:3} 

        #Initiate an empty array to store the results
        res = []

        #Iterate num to calculate the frequency of each num
        for num in nums:
            freq_count[num] = 1 + freq_count.get(num, 0) #If num is already in freq_count, then append 1 to the frequency

        for i in range(0, k):
            max_key = max(freq_count, key=freq_count.get)
            res.append(max_key)
            freq_count.pop(max_key)
        
        return res
        
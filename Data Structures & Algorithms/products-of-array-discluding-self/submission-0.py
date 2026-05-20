class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #loop through array and get the product. go throough it again and divide
        # prod = 1
        # for num in nums:
        #     prod *= num

        # products = []
        # for num in nums:
        #     products.append(prod//num)

        # return products



        #keep a prefix and suffix arrays where you keep track of the product before number 
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        pre_prod = 1
        for i in range(len(nums)):
            prefix[i] = pre_prod
            pre_prod *= nums[i]

        suff_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suff_prod
            suff_prod *= nums[i]


        products = []
        for i in range(len(prefix)):
            products.append(prefix[i] * suffix[i])

        return products
            


        
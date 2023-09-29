input_data = [0,0]
prefix_data = []
postfix_data = []
output_data = []

for index in range(len(input_data)):
    
    reverse_index = len(input_data)-index
    
    if index == 0 or reverse_index == len(input_data):
        prefix_data.append(input_data[index])
        postfix_data.insert(0, input_data[reverse_index-1])
        continue
        
    prefix_data.append(prefix_data[len(prefix_data)-1] * input_data[index])
    postfix_data.insert(0, postfix_data[0]*input_data[reverse_index-1])
    
for index in range(len(input_data)):
    prefix = 1
    postfix = 1
    
    if index >= 1:
        prefix = prefix_data[index-1]
    if index != len(input_data) - 1:
        postfix = postfix_data[index+1]
        
    output_data.append(prefix*postfix)
    
    
    
print(prefix_data)
print(postfix_data)
print(output_data)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_data = []
        for index in range(len(nums)):
            if index == 0:
                output_data.append(1)
                continue
                
            output_data.append(nums[index-1]*output_data[len(output_data)-1])
            
        post_fix = 1
        for index in range(len(output_data)):
            reverse_index = len(output_data)-(index+1)
            
            output_data[reverse_index] = output_data[reverse_index] * post_fix
            
            post_fix *= nums[reverse_index]

        return output_data
    
    
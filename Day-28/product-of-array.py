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

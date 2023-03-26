# Largest rectangle in histogram problem 


heights = [3,2,4,5,7,6,1,3,8,9,10,11,10,7,5,2,6]

def largest_rectangle(heights):
    heights = [-1]+heights+[-1]
    max_area = 0
    stack = [(0, -1)]
    for i in range(1, len(heights)):
        start = i
        while stack[-1][1] > heights[i]:
            top_index, top_height = stack.pop()
            max_area = max(max_area, top_height*(i-top_index))
            start = top_index
        stack.append((start, heights[i]))
    return max_area

print(largest_rectangle(heights))
import random
class Solution:
    def stack_boxes(self, boxes):
        def can_stack(box1, box2):
            return box2[0] < box1[0] and box2[1] < box1[1]

        heights = {box:[box[2], [box]] for box in boxes}
        sboxes = sorted(boxes, key=lambda x: x[1], reverse=True)
        max_height = sboxes[0][2]
        max_height_list = [sboxes[0]]
        for i in range(0,len(sboxes)):
            for j in range(i+1, len(sboxes)):
                if can_stack(sboxes[i], sboxes[j]):
                    heights[sboxes[i]][0] += heights[sboxes[j]][0]
                    heights[sboxes[i]][1].append(sboxes[j])

            if heights[sboxes[i]][0] > max_height:
                max_height = heights[sboxes[i]][0]
                max_height_list = heights[sboxes[i]][1]

        return [max_height, max_height_list]

def generateInputs():
    inputs = []
    r = lambda lo, hi: random.randint(1,10)
    for _ in range(10):
        inputs.append([(r(1,10), r(1,10), r(1,10)) for _ in range(r(5,20))])
    return inputs

inputs = generateInputs()
#boxes1 = [(4, 3, 5), (9, 5, 1), (5, 5, 7), (8, 6, 9)]

s = Solution()
for input in inputs:
    res = s.stack_boxes(input)
    s_input = sorted(input, key=lambda x: x[0], reverse=True)
    print(f'input: {s_input}, output: {res[0]}, {res[1]}\n')


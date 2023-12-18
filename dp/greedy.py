def canJump(nums):
    max_reach = 0  # 记录当前能够到达的最远位置

    for i in range(len(nums)):
        # 如果当前位置超过了最远位置，表示无法到达当前位置，返回 False
        if i > max_reach:
            return False

        # 更新最远位置
        max_reach = max(max_reach, i + nums[i])

        # 如果最远位置已经可以到达数组末尾，返回 True
        if max_reach >= len(nums) - 1:
            return True

    return True


# 测试示例
nums = [2, 3, 1, 1, 0, 4]
result = canJump(nums)
print(result)  # 输出 True

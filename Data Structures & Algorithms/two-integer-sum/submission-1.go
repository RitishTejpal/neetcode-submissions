func twoSum(nums []int, target int) []int {
    mp := make(map[int]int)
    for i := 0; i < len(nums); i++ {
        num := nums[i]
        complement := target - num
        if idx, ok := mp[complement]; ok {
            return []int{idx, i}
        }
        mp[num] = i
    }
    
    return []int{}
}
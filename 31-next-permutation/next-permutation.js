
 
 
var nextPermutation = function(nums) {
    const n = nums.length;

    
    
    let pivot = n - 2;
    while (pivot >= 0 && nums[pivot] >= nums[pivot + 1]) {
        pivot--;
    }

    
    if (pivot >= 0) {
        
        let successor = n - 1;
        while (nums[successor] <= nums[pivot]) {
            successor--;
        }

        
        [nums[pivot], nums[successor]] = [nums[successor], nums[pivot]];
    }

    let left = pivot + 1;
    let right = n - 1;

    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]];
        left++;
        right--;
    }

    return nums; 
};

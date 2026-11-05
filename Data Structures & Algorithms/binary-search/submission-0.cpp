#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());

        int left = 0;
        int right = nums.size() - 1;

        while(left<=right){
            int middle = (left+right)/2;
            if(nums[middle] == target){
                return middle;
            }else if(nums[middle]>target){
                right = middle-1;
            }else if(nums[middle]<target){
                left = middle+1;
            }
        }
        return -1;
        
    }
};
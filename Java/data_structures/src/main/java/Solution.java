class Solution {
    public int[] twoSum(int[] nums, int target) {
        int temp = 0;
        int [] ret = new int[2];
        outerloop:
        for (int i = 0; i < nums.length; i ++){
            for(int k = 0; k < nums.length; k++){
                if( i != k){
                    temp = nums[i] + nums[k];
                    if( temp == target){
                        ret[0] = i;
                        ret[1] = k;
                        break outerloop;
                    }
                }
            }
        }
        return ret;
    }

    public static void main(String args[]){

        Solution sol = new Solution();
        int[] arr = {2,7,11,15};
        int[] sols= sol.twoSum(arr, 9);
        System.out.println(sols[0]+" "+ sols[1]);

        arr = new int[]{3, 2, 4};
        sols= sol.twoSum(arr, 6);
        System.out.println(sols[0]+" "+ sols[1]);
    }
}
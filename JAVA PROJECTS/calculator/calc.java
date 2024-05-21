//FIX IR WITH ODD NUMBERS
import java.util.Arrays;
import java.lang.Math;

public class calc {
    public static void main(String args[]) {
        double nums[] = {2, 5, 34, 83, 103, 120};
        Arrays.sort(nums);
        min(nums);
        max(nums);
        mean(nums);
        median(nums);
        ir(nums); //interquartile range
        sd(nums); //standard deviation
        variance(nums);
    }
    public static void min(double nums[]) {
        double min = nums[0];
        min = (double)Math.round(min*1000d)/1000d;
        System.out.println("min: " + min);
    }
    public static void max(double nums[]) {
        double max = nums[nums.length-1];
        max = (double)Math.round(max*1000d)/1000d;
        System.out.println("max: " + max);
    }
    public static void mean(double nums[]) {
        double mean = 0;
        for (double a : nums) {
            mean += a;
        }
        mean /= nums.length;
        mean = (double)Math.round(mean*1000d)/1000d;
        System.out.println("mean: " + mean);
    }
    public static void median(double nums[]) {
        double median = 0;
        if (nums.length % 2 == 0) {
            median = (nums[nums.length/2] + nums[nums.length/2 - 1])/2;
        } else {
            median = nums[(nums.length)/2];
        }
        median = (double)Math.round(median*1000d)/1000d;
        System.out.println("median: " + median);
    }
    public static void ir(double nums[]) {
        //median
        double median = 0;
        if (nums.length % 2 == 0) {
            median = (nums[nums.length/2] + nums[nums.length/2 - 1])/2;
        } else {
            median = nums[(nums.length)/2];
        }
        median = (double)Math.round(median*1000d)/1000d;
        //interquartile range
        double ir = 0;
        if (nums.length % 2 == 0) {
            double nums1[] = new double [nums.length/2];
            double nums2[] = new double [nums.length/2];
            for (int i = 0; i < nums.length/2; i++) {
                nums1[i] = nums[i];
            }
            for (int i = 0; i < nums.length - nums.length/2; i++) {
                nums2[i] = nums[i + nums.length/2];
            }
            //medians of nums1 and nums2
            if (nums1.length % 2 == 0) {
                ir += (nums1[nums1.length/2] + nums1[nums1.length/2 - 1])/2;
            } else {
                ir += nums1[(nums1.length)/2];
            }
            if (nums.length % 2 == 0) {
                ir += (nums2[nums2.length/2] + nums2[nums2.length/2 - 1])/2;
            } else {
                ir += nums2[(nums2.length)/2];
            }
        } else {
            double nums1[] = new double [nums.length/2];
            double nums2[] = new double [nums.length/2];
            for (int i = 0; i < nums.length/2; i++) {
                nums1[i] = nums[i];
            }
            for (int i = 0; i < nums.length - nums.length/2; i++) {
                nums2[i] = nums[i + nums.length/2];
            }
            //medians of nums1 and nums2
            if (nums1.length % 2 == 0) {
                ir += (nums1[nums1.length/2] + nums1[nums1.length/2 - 1])/2;
            } else {
                ir += nums1[(nums1.length)/2];
            }
            if (nums.length % 2 == 0) {
                ir += (nums2[nums2.length/2] + nums2[nums2.length/2 - 1])/2;
            } else {
                ir += nums2[(nums2.length)/2];
            }
        }
        ir = (double)Math.round(ir*1000d)/1000d;
        System.out.println("ir: " + ir);
    }
    public static void sd(double nums[]) {
        //mean
        double mean = 0;
        for (double a : nums) {
            mean += a;
        }
        mean /= nums.length;
        mean = (double)Math.round(mean*1000d)/1000d;
        //standard deviation
        double sd = 0;
        for (int i = 0; i < nums.length; i++) {
            sd += Math.pow(nums[i] - mean,2);
        }
        sd /= nums.length;
        sd = Math.sqrt(sd);
        sd = (double)Math.round(sd*1000d)/1000d;
        System.out.println("sd: " + sd);
    }
    public static void variance(double nums[]) {
        //mean
        double mean = 0;
        for (double a : nums) {
            mean += a;
        }
        mean /= nums.length;
        mean = (double)Math.round(mean*1000d)/1000d;
        //standard deviation
        double variance = 0;
        for (int i = 0; i < nums.length; i++) {
            variance += Math.pow(nums[i] - mean,2);
        }
        variance /= nums.length;
        variance = (double)Math.round(variance*1000d)/1000d;
        System.out.println("variance: " + variance);
    }
}
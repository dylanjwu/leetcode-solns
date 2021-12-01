
/**
  Top down and bottom up versions included
*/

class Solution {
    private int diff(char a, char b){
        if (a == b) return 0;
        return 1;
    }
    
    public int topDown(String word1, int i, String word2, int j, int[][] dp){
        
        if (i >= word1.length() && j >= word2.length()) return 0;
        
        if (i >= word1.length()) return word2.length()-j;
        if (j >= word2.length()) return word1.length()-i;
        
        if (dp[i][j] == -1){
            int left = 1+topDown(word1, i+1, word2, j, dp);
            int right = 1+topDown(word1, i, word2, j+1, dp);
            int firstMin = Math.min(left, right);
        
            int both = diff(word1.charAt(i), word2.charAt(j))+topDown(word1, i+1, word2, j+1, dp); 
            dp[i][j] = Math.min(firstMin, both);
        }
        return dp[i][j];
    }
    
    
    public int bottomUp(String word1, String word2){
        int[][] dp = new int[word1.length()+1][word2.length()+1];
        for (int i = 1; i < dp.length; i++){
            for (int j = 1; j < dp[0].length; j++){
                if (i == 1) dp[i-1][j] = j;
                if (j == 1) dp[i][j-1] = i;
                int firstMin = 1 + Math.min(dp[i-1][j], dp[i][j-1]);
                int secMin = diff(word1.charAt(i-1), word2.charAt(j-1)) + dp[i-1][j-1];
                dp[i][j] = Math.min(firstMin, secMin);
            }
        }
        return dp[dp.length-1][dp[0].length-1];
    }
    
    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word1.length()+1][word2.length()+1];
        for (int i = 0; i < dp.length; i++){
            for (int j = 0; j < dp[0].length; j++){
                dp[i][j] = -1;
            }
        }
        
        
        if (word1.length() == 0) return word2.length();
        if (word2.length() == 0) return word1.length();
        return topDown(word1, 0, word2, 0, dp);
        //return bottomUp(word1, word2);
    }
}

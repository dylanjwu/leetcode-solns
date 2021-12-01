/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
*/

//bottom up version
var longestCommonSubsequence = function(text1, text2) {
    let dp = new Array(text1.length+1)
        .fill(null).map(el => new Array(text2.length+1).fill(0));
    
    for (let i = 1; i < dp.length; i++){
        for (let j = 1; j < dp[0].length; j++){
            if (text1[i-1] == text2[j-1]){
                dp[i][j] = 1 + dp[i-1][j-1];
            }
            else
                dp[i][j] += Math.max(dp[i-1][j], dp[i][j-1]);
        }
    }
    console.log(dp);
    return dp[dp.length-1][dp[0].length-1];
}

/*
top down version
var longestCommonSubsequence = function(text1, text2) {
    var dp = Array(text1.length).fill(null).map(arr => Array(text2.length).fill(-1));
    var helper = function(i, j){
        if (i >= text1.length || j >= text2.length)
            return 0;
        
        if (dp[i][j] == -1){
            if (text1[i] === text2[j])
                dp[i][j] = 1 + helper(i+1,j+1);
            else
                dp[i][j] = Math.max(helper(i+1, j), helper(i, j+1));
        }
        return dp[i][j]
    }
    return helper(0,0);
};
*/

int minDominoRotations(int* tops, int topsSize, int* bottoms, int bottomsSize){
    
    int possible_moves[2] = {tops[0], bottoms[0]};
    int top_moves[2] = {0, 0};
    int bottom_moves[2] = {0, 0};
    
    int i;
    for (i=0; i < topsSize; i++){
        
        int j;
        for (j=0; j < 2; j++){
            int domino = possible_moves[j];
            if (tops[i] == domino && bottoms[i] == domino)
                continue;
                
            else if (tops[i] == domino){
                bottom_moves[j] += 1;
            }
                 
            else if (bottoms[i] == domino){
                top_moves[j] += 1;
            }
            else {
                possible_moves[j] = -1;
                bottom_moves[j] = 0;
                top_moves[j] = 0;
            }
        }
        if (possible_moves[0] == -1 && possible_moves[1] == -1) 
            return -1;
    }
    
    
    int min_top = (top_moves[0] < top_moves[1] ? top_moves[0] : top_moves[1]);
    if (min_top == 0) min_top = (top_moves[0] > top_moves[1] ? top_moves[0] : top_moves[1]);
 
    
    int min_btm = (bottom_moves[0] < bottom_moves[1] ? bottom_moves[0] : bottom_moves[1]);
    if (min_btm == 0) min_btm = (bottom_moves[0] > bottom_moves[1] ? bottom_moves[0] : bottom_moves[1]);
    
    return (min_top > min_btm) ? min_btm : min_top;

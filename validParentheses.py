class Solution {
public:
    bool isValid(string s) {
        stack<char> history;
        unordered_map<char, char> pairs;
        pairs['{'] = '}';
        pairs['('] = ')';
        pairs['['] = ']';
    
        if(s.length() == 0) return true;
        if(s.length() % 2 != 0) return false;
        
        for(int e = 0; e < s.length(); e++) {
            if(history.empty()) history.push(s[e]);
            else {
                if(pairs[history.top()] == s[e]) history.pop();
                else history.push(s[e]);
            }
        }
        
        if(history.empty()) return true;
        else return false;
        
    }
};

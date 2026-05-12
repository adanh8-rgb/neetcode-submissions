class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }
        for(char c : s) {
            bool found = false;
            for(int i = 0; i < t.size(); i++) {
                if(t[i] == c) {
                    found = true;
                    t.erase(i,1);
                    break;
                }
            }
            if(!found) {
                return false;
            }
        }
        return true;
    }
};

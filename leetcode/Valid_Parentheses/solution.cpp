class Solution {
public:
    bool isValid(string s) {
        if (s.length() % 2 != 0)
            return false;
        
        map<char, char> hash = {{'(', ')'}, {'[', ']'}, {'{', '}'}};
        stack<char> elements;
        for (auto el : s){
            if (hash.find(el) != hash.end())
                elements.push(el);
            else{
                if (elements.size() == 0)
                    return false;
                char a = elements.top(); 
                elements.pop();
                if (el != hash.at(a))
                    return false;
            }
        }
        
        return elements.size() == 0;
     
    }
};
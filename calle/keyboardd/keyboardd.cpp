#include <iostream>
#include <string>

using namespace std; 

int main(){
  string s, t; 
  getline(cin, s); 
  getline(cin, t);
  s += '%'; 
  t += '%'; 
  int j = 0; 
  string res; 
  for(int i = 0; i<s.length(); i++){
    if(s[i] != t[j]){
      if(res.find(t[j]) == std::string::npos)
        res += t[j]; 
      while(s[i] != t[j])
        j++; 
    }
    j++; 
  }
  cout << res << endl; 
}

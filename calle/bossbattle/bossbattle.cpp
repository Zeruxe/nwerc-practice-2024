#include <iostream>

using namespace std; 

int main(){
  int n; 
  cin >> n; 
  if(n == 2){
    cout << 1 << endl; 
    return 0; 
  }

  int boss, bomb; 
  bomb = 0; 
  boss = n-2; 
  int res = 0; 
  while(1){
    if(bomb == boss)
      break; 
    boss++; 
    bomb += 2;

    boss %= n; 
    bomb %= n; 
    res++; 
  }
  cout << res << endl; 

}

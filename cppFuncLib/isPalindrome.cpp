#include <iostream>
#include <string>
//using namespace std;

int isPalindrome(std::string s){
    /*
    return 1 if the input string is a palindrome, else return 0.
    */
    if(s.length() == 1)
        return 1;
    int i = 0;
    int j = s.length() - 1;
    while(i <= j){
        if(s[i] == s[j]){
            i++; j--;
        }
        else
            return 0;
    }
    return 1;
}
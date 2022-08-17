#include <vector>
#include <stdexcept>
#include <iostream>

bool sortcol(const vector<int>& v1, const vector<int> v2){
    // if(col >= v1.size() || col >= v2.size()){
    //     throw std::runtime_error("Column index exceed the limit.");
    // }
    return v1[1] < v2[1];
}


void vectorSort(std::vector<std::vector<int>>& nums){
    // sort the vector based on the second column
    std::sort(nums.begin(), nums.end(), sortcol);
}


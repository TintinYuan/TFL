#include <iostream>
#include <algorithm>
int partition(int arr[], int start, int end){
    int pivot = arr[start];
    int count = 0;
    for(int i = start + 1; i <= end; i++){
        if(arr[i] <= pivot)
            count++; // calculate the position of pivot
    }

    int pivotIndex = start + count; // the new position of pivot
    std::swap(arr[pivotIndex], arr[start]);
    
    int i = start, j = end;
    while(i < pivotIndex && j > pivotIndex){
    	while(arr[i] <= pivot){
	    i++;
	}
	while(arr[j] > pivot){
	    j--;
	}
	if(i < pivotIndex && j > pivotIndex){
	    std::swap(arr[i++], arr[j--]);
	}
	return pivotIndex;
    }
}

void quickSort(int arr[], int start, int end){
    // base case
    if(start >= end)
	return;

    // partitioning the array
    int p = partition(arr, start, end);

    // sort the left part
    quickSort(arr, start, p - 1);

    // sort the right part
    quickSort(arr, p + 1, end);
}


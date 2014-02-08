---
layout: post
title: "Find Missing Number In Two Arrays"
date: 2014-01-17 1:00
category: Electrical Engineering
tags: [Numbers, C, Interview, Electrical Engineering]
---

# Question

You are given two arrays representing two sets of numbers.
The numbers are in any order, may have duplicates, and are
not necessarily consecutive.

The two arrays should have the same set of numbers but one
number is missing.

Write a C program to find the missing number.

# Answer

The first approach is to sort the arrays and scan them for
the missing number.

{% highlight c %}
#include <stdio.h>

void sort(unsigned int* arr, unsigned int size) {
    unsigned int i;
    unsigned int tmp;
    unsigned char not_sorted = 1;

    while (not_sorted) {
        not_sorted = 0;  // default, assume sorted
        for (i = 1; i < size; i++) {
            if (arr[i] < arr[i-1]) {
                // swap the values
                tmp = arr[i];
                arr[i] = arr[i-1];
                arr[i-1] = tmp;
                not_sorted = 1;
            }
        }
    }
}

#define szA 5
#define szB 4

int main() {

    unsigned int missing;
    unsigned int i;

    unsigned int A[szA] = {1, 50, 2, 175, 45};
    unsigned int B[szB] = {45, 175, 2, 1};

    sort(A, szA);
    sort(B, szB);

    unsigned int min_sz = (szA > szB) ? szB : szA;

    // scan both to find missing number
    for (i = 0; i < min_sz; i++) {
        if (A[i] != B[i]) {
            // found missing number
            missing = (szA > szB) ? A[i] : B[i];
            break;
        }
    }
    // check if missing number in end of longer array
    if (i == min_sz) {
        missing = (szA > szB) ? A[szA-1] : B[szB-1];
    }

    printf("missing: %i\n", missing);

    return 0;
}
{% endhighlight %}

Everyone I have discussed this problem with arrives at this solution.

The second solution is to take the sum of each array and subtract
the one with the extra element from the one with the missing
element.  The difference is the missing number.

{% highlight c %}
#include <stdio.h>

unsigned int sum(unsigned int* array, unsigned int size) {
	unsigned int i;
	unsigned int sum;

	sum = 0;
	for (i = 0; i < size; i++) {
		sum = sum + array[i];	
	}

	return sum;
}

#define szA 5
#define szB 4

int main() {

	unsigned int missing;

	unsigned int A[szA] = {1, 50, 2, 175, 45};
	unsigned int B[szB] = {45, 175, 2, 1};

	unsigned int sumA;	
	unsigned int sumB;	

	sumA = sum(A, szA);
	sumB = sum(B, szB);

	missing = sumA - sumB;

	printf("missing: %i\n", missing);

	return 0;
}
{% endhighlight %}

# Background

This question was given during an in person interview on 1/17/2014 for
a firmware test engineer position.

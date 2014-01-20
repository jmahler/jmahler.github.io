---
layout: post
title: "Find Missing Number In Two Arrays"
date: 2014-01-17 1:00
category: Electrical Engineering
tags: Numbers, C, Interview, Electrical Engineering
---

# Question

You are given two arrays which should be equal but one
is missing a number.

Write a C program to find the missing number.

# Answer

The answer is simple.
Take the sum of each set and then subtract the one with
the extra element from the one with the missing element.
The result is the missing number.

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

This question was given during an interview on 1/17/2014 for
a firmware test engineer position.

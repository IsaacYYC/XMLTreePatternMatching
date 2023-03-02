/*
 * TreeQuery.cpp
 *
 *  Created on: Mar. 2, 2023
 *      Author: Isaac Martens, Brett Wells
 */

#include <iostream>
#include <bits/stdc++.h>
#include <vector>
#include "TreeQuery.h"

int main() {

std::vector<*TreeQuery> queries;
int testRuns;

std::cout << "enter number of test runs per query\n"
std::cin >> testRuns;

for (*TreeQuery : it) {
	double totalTimeTaken = 0;
	for (int i = 0;i < testRuns; i++) {
		time_t start, end;
		time(&start);
		//query function
		time(&end);

		double timeTaken = double(end - start);
		totalTimeTaken += timeTaken;
		std::cout << "Time taken by query of " << "it.TreeQuery->fileSize" << " size " << fixed << timeTaken << setprecision(5);
		std::cout << " seconds\n";
	}
	std::cout << "Average time taken " << fixed << totalTimeTaken / testRuns << setprecision(5);
	std::cout << " seconds\n\n";
}

  return 0;
}

#ifndef INCLUDE_TREEMATCHUTILITY_H_
#define INCLUDE_TREEMATCHUTILITY_H_

#include <cctype>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include "tinyxml2.h"

using namespace tinyxml2;

bool isLeaf(XMLNode* q) {
	return q->NoChildren();
};

int numOfChildren(XMLNode* q) {
	int count = 0;
	if (q == nullptr) return 0;
	XMLNode* first = q->FirstChild();
	if (first == nullptr) return 0;
	count++;
	XMLNode* next;
	next = first->NextSibling();
	if (next == nullptr) return count;
	count++;
	while(true) {
		next = next->NextSibling();
		if (next == nullptr) return count;
		count++;
	}
};

#endif /* INCLUDE_TREEQUERY_H_ */

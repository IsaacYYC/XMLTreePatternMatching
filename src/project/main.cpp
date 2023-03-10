/* Testing123*/

#include <iostream>
#include "tinyxml2.h"
#include "TreeMatchUtility.h"
#include <cerrno>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace tinyxml2;

int main() {
	std::cout << "Hello World" << std::endl;

	XMLDocument doc;
	bool b = doc.LoadFile( "data/sample.xml" );
	std::cout << b << std::endl;
	doc.PrintError();
	doc.Print();
	std::cout << doc.RootElement()->Name() << std::endl;
	std::cout << isLeaf(doc.RootElement()) << std::endl;
	std::cout << numOfChildren(doc.RootElement()) << std::endl;

	/*XMLText* textNode = doc.FirstChildElement( "employee" )->FirstChildElement( "id" )->FirstChild()->ToText();
	const char* id = textNode->Value();
	printf( "Name of play (2): %s\n", id );*/
	return 0;
}

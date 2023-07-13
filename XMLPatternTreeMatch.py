import xml.etree.ElementTree as ET

def isLeaf(q):
    return (q.find('*') == None)

def searchPattern(qi, p):#searches pattern to see if current node from query exists
    for pi in p:
        #print("search comparison: ", child.tag, pi.tag)
        if (pi.tag == qi.tag):
            return pi
    return None

#root is the root object of the item found in the query, this function will print only children that were also found 
def printResults(root, sln):
    for element in root.iter():
        if element.tag in sln:
            print(f"{element.tag}: {element.text}")

def find(q, p, sln):
    #if node is a leaf, check match and add to solution
    if (isLeaf(p)):
        if (q.tag == p.tag):
            if (q.tag in sln):
                sln[q.tag].append(q)
                return True
            else:
                sln[q.tag] = [q]
                return True
        else: 
            return False

    #do all elements of next level pattern exist in data
    for pi in p:
        if (q.find(pi.tag) == None):
            return False

    #iterate through data on this level, checking matches and adding to solution
    allChildrenMatch = True
    for qi in q: 
        pi = searchPattern(qi, p)
        if (pi != None):
            allChildrenMatch = find(qi, pi, sln)
            if (allChildrenMatch):
                if (qi.tag in sln):
                    sln[qi.tag].append(qi)
                else:
                    sln[qi.tag] = [qi]
    return allChildrenMatch
# TSP
There are n cities 1, 2, ..., n. The travel distance from city i to city j is c(i,j), for i,j = 1, 2, ..., n.  A person departs from city 1, visits each city 2, 3, ..., n exactly once and comes back to city 1. Find the itinerary for that person so that the total travel distance is minimal. <br/>
A solution is represented by a sequence of n variables x[1], x[2], . . ., x[n] in which the tour is: x[1] -> x[2] -> . . . -> x[n] -> x[1].<br/>

# Input <br/>
Line 1: a positive integer n (1 <= n <= 200) <br/>
Line i+1 (i = 1, . . ., n): contains the ith row of the distance matrix x (elements are separated by a SPACE character) <br/>

# Output <br/>
Line 1: write the value n <br/>
Line 2: write x[1], x[2], . . ., x[n] (after each element, there is a SPACE character) <br/>

# Example
Input <br/>
4 <br/>
0 1 1 9 <br/>
1 0 9 3 <br/>
1 9 0 2 <br/>
9 3 2 0 <br/>
Output <br/>
4 <br/>
1 3 4 2 <br/>


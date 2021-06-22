// C++ program to find number of cells a queen can move
// with obstacles on the chessborad
#include<bits/stdc++.h>
using namespace std;

// Return if position is valid on chessboard
int range(int n, int x, int y)
{
return (x <= n && x > 0 && y <= n && y > 0);
}

// Return the number of moves with a given direction
int check(int n, int x, int y, int xx, int yy,
				map <pair<int, int>, int> mp)
{
int ans = 0;

// Checking valid move of Queen in a direction.
while (range(n, x, y) && ! mp[{x, y}])
{
	x += xx;
	y += yy;
	ans++;
}

return ans;
}

// Return the number of position a Queen can move.
int numberofPosition(int n, int k, int x, int y,
				int obstPosx[], int obstPosy[])
{
int x1, y1, ans = 0;
map <pair<int, int>, int> mp;

// Mapping each obstacle's position
while(k--)
{
	x1 = obstPosx[k];
	y1 = obstPosy[k];
	
	mp[{x1, y1}] = 1;
}

// Fetching number of position a queen can
// move in each direction.
ans += check(n, x + 1, y, 1, 0, mp);
ans += check(n, x-1, y, -1, 0, mp);
ans += check(n, x, y + 1, 0, 1, mp);
ans += check(n, x, y-1, 0, -1, mp);
ans += check(n, x + 1, y + 1, 1, 1, mp);
ans += check(n, x + 1, y-1, 1, -1, mp);
ans += check(n, x-1, y + 1, -1, 1, mp);
ans += check(n, x-1, y-1, -1, -1, mp);

return ans;
}

// Driven Program
int main()
{
int n = 8; // Chessboard size
int k = 1; // Number of obstacles
int Qposx = 4; // Queen x position
int Qposy = 4; // Queen y position
int obstPosx[] = { 3 }; // x position of obstacles
int obstPosy[] = { 5 }; // y position of obstacles

cout << numberofPosition(n, k, Qposx, Qposy,
				obstPosx, obstPosy) << endl;
return 0;
}

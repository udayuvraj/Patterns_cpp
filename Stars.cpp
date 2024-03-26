// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

void print0() {
	int n;
	cin >>n;
	for(int i = 0 ;i <n;i++)
	{
		for(int j = 0;j<n;j++)
		{
			cout << "*";
		}
		cout << endl;
	}
}

void print1()
{
	int n;
	cin >>n;
	for(int i =0;i<n;i++)
	{
		for(int j =0;j<=i;j++)
		{
			cout << "*";
		}
		cout << endl;
	}
}
void print2()
{
	int n;
	cin >>n;
	for(int i =1;i<=n;i++)
	{
		for(int j =1;j<=i;j++)
		{
			cout << j;
		}
		cout << endl;
	}
}
void print3()
{
	int n;
	cin >>n;
	for(int i =1;i<=n;i++)
	{
		for(int j =1;j<=i;j++)
		{
			cout << i;
		}
		cout << endl;
	}
}
void print4()
{
	int n;
	cin >>n;
	for(int i =0;i<n;i++)
	{
		for(int j =n;j>i;j--)
		{
			cout << "*";
		}
		cout << endl;
	}
}
void print5()
{
	int n;
	cin >>n;
	for(int i =0;i<=n;i++)
	{
		for(int j =n;j>i;j--)
		{
			cout << n-j+1;
		}
		cout << endl;
	}
}
void print6()
{
	int n;
	cin >> n;
	for(int i =0;i<n;i++)
	{
		//space
		for(int j =0;j<n-i-1;j++)
		{
			cout << " ";
		}
		//star
		for(int j =0;j<2*i+1;j++)
		{
			cout << "*";
		}
		//space
		for(int j =0;j<n-i-1;j++)
		{
			cout << " ";
		}
		cout<<endl;
	}
}
void print7()
{
	int n;
	cin >> n;
	for(int i =0;i<n;i++)
	{
		//space
		for(int j =0;j<i;j++)
		{
			cout << " ";
		}
		//star
		for(int j =0;j< 2*n -(2*i+1);j++)
		{
			cout << "*";
		}
		//space
		for(int j =0;j<i;j++)
		{
			cout << " ";
		}
		cout<<endl;
	}
}
void print8()
{
	int n;
	cin >> n;
	for(int i =0;i<n;i++)
	{
		//space
		for(int j =0;j<n-i-1;j++)
		{
			cout << " ";
		}
		//star
		for(int j =0;j<2*i+1;j++)
		{
			cout << "*";
		}
		//space
		for(int j =0;j<n-i-1;j++)
		{
			cout << " ";
		}
		cout<<endl;
	}
		for(int i =0;i<n;i++)
	{
		//space
		for(int j =0;j<i;j++)
		{
			cout << " ";
		}
		//star
		for(int j =0;j< 2*n -(2*i+1);j++)
		{
			cout << "*";
		}
		//space
		for(int j =0;j<i;j++)
		{
			cout << " ";
		}
		cout<<endl;
	}

}

void print9()
{
	int n;
	cin >> n;
	for(int i =0;i<n;i++)
	{
		for(int j = 0;j<=i;j++)
		{
			cout <<"*";
		}
		cout << endl;
	}
	for(int i =0;i<n-1;i++)
	{
		for(int j = n-1;j>i;j--)
		{
			cout <<"*";
		}
		cout << endl;
	}
}
void print10()
{
	int n;
	cin >> n;
    int spaces = 2*n-2;
      for(int i = 1;i<=2*n-1;i++){
          
          // stars for first half
          int stars = i;
          
          // stars for the second half.
          if(i>n) stars = 2*n - i;
          
          //stars
          for(int j=1;j<=stars;j++){
              cout<<"*";
          }
          
          //spaces
          for(int j = 1;j<=spaces;j++){
              cout<<" ";
          }
          
          //stars
          for(int j = 1;j<=stars;j++){
              cout<<"*";
          }
          
          
          cout<<endl;
          if(i<n) spaces -=2;
          else spaces +=2;
      }
      
}


int main()
{	
	print0();
	print1();
	print2();
	print3();
	print4();
	print5();// purely help taken in this "because i didn't get!!"
	print6();
	print7();
	print8();
	print9();
	print10(); // butterfly

}
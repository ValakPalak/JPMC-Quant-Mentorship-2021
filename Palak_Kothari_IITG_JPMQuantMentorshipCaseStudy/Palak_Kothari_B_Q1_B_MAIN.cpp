#include<bits/stdc++.h>
using namespace std;

map<int, int> rule;
vector<int> seed_grid;

void initialise_seed_grid(int size, vector<int> &v){
	seed_grid.clear();
	seed_grid.resize(size);
	seed_grid = v;
	return;
}


void initialise_rule(vector<int> &v){
	rule.clear();
	int n = v.size();
	for(int i=0;i<n;++i){
		rule[i] = v[i];
	}
	return;
}


void next_gen(vector<int> &gen){
	
	vector<int> curr(gen);
	int n = curr.size(), parent;

	for(int i=0;i<n;++i){
		parent = curr[(n+i-1)%n]*4   +   curr[i]*2   +  curr[(i+1)%n];
		gen[i] = rule[parent];
	}
	return;
}

int main(){

	int grid_size = 4;
	vector<int> seed_gen = {1,1,0,0}, rule_values = {1,1,0,0,1,0,1,0};
	initialise_seed_grid(grid_size, seed_gen);
	initialise_rule(rule_values);

	int generation = 4;
	vector<int> gen(seed_gen);
	for(int i=0; i<generation; ++i){
		next_gen(gen);
		for(int i=0;i<grid_size;++i){
			if(gen[i]==1) 
				cout << '|';
			else if(gen[i] == 0)
				cout << '.'; 
		}
		cout<<endl;	
	}

	return 0;
}
#include<bits/stdc++.h>
using namespace std;



vector<int> seed_grid; //contains the seed generation configuration of the grid
map<int,double> rule; //contains probability for having 0 in the cell in next generation
map<int, vector<int>> state;//state number to configuration
vector<vector<double>> prob; //Stores the transition matrix
vector<vector<double>> prob_k; 

//To initialise the seed grid
void initialise_seed_grid(int size, vector<int> &v){
	seed_grid.clear();
	seed_grid.resize(size);
	seed_grid = v;
	return;
}

//To Fill The Rule Table
void initialise_rule(vector<double> &v){
	rule.clear();
	int n = v.size();
	for(int i=0;i<n;++i){
		rule[i] = v[i];
	}
	return;
}


int start_state(vector<int> &v){
	int n = v.size();
	int ans = 0;
	int p = 1;
	for(int i=n-1;i>=0;--i){
		ans += v[i]*p;
		p*=2;
	}
	return ans;
}

void add_one(vector<int> &v){
	//add one in the binary number stored in v
	int n = v.size();
	int carry = 1;
	for(int i=n-1; i>=0; --i){
		if(v[i]+carry == 2){
			v[i] = 0;
			carry = 1;
		}
		else {
			v[i] = v[i]+carry;
			carry = 0;
		}
	}
	return;
}

void binary(int n){
	string s = "";
	if(n==0) {
		s = '0';
		cout<<s<<"\n";
		return;
	}
	int len = floor(log2(n))+1;
	for(int i = 0; i < len ; ++i){
		if(n & (1<<i)) s += '1';
		else s += '0';
	}
	reverse(s.begin(), s.end());
	cout<<s<<"\n";
	return;
}


void initialise_state(int n){
	// n is grid size
	int size = (int)pow(2,n); // number of states
	vector<int> v(n);
	state[0] = v;
	for(int i=1;i<size;++i){
		add_one(v);
		state[i] = v;
	}
	return;
}


//Calculates Transition Matrix
void preprocess_probability(int n){
	int size = (int)pow(2,n), parent; //number of states
	
	prob.resize(size, vector<double>(size));
	for(int i=0;i<size;++i){
		for(int j=0; j<size; ++j){
			prob[i][j] = 1.0;
			vector<int> statei = state[i];
			vector<int> statej = state[j];
			for(int k=0; k<n; ++k){
				parent = statei[(n+k-1)%n]*4 + statei[k]*2 + statei[(k+1)%n];
				if(statej[k] == 0) prob[i][j] *= rule[parent];
				else prob[i][j] *= (1-rule[parent]);
			}
		}
	}

	return;
}

//Multipluy two matrices and store them 2-D vector prob_k
void multiply(vector<vector<double>> &res, vector<vector<double>> a, vector<vector<double>> b){
	for(int i=0;i<a.size();++i){
		for(int j=0;j<b.size();++j){
			res[i][j] = 0.0;
			for(int k = 0; k<a[0].size();++k){
				res[i][j] += a[i][k]*b[k][j];
			}
		}
	}
	return;
}	

void identity_matrix(vector<vector<double>> &a, int size ){
	for(int i = 0;i<size;++i)
		a[i][i] = 1.0;
	return;
}

//Calculate M^k in O(logk) time where M is a matrix
void binary_exponentiation(int n, int st, int k){
	int size = (int)pow(2,n); //number of states
	prob_k.resize(size, vector<double>(size));
	vector<vector<double>> res(size, vector<double>(size, 0.0));
	identity_matrix(res,size);
	vector<vector<double>> temp(size, vector<double>(size, 0.0));
	temp = prob;
	while(k>0){
		if(k&1){
			multiply(res, res, temp);
		}
		multiply(temp,temp,temp);
		k>>=1;	
	}
	prob_k.clear();
	prob_k = res;
	return;
}

void print(){


	return; 

}

int main(){

	int grid_size = 4;
	int total_states = (int)pow(2,grid_size);
	int generation = 1;
	int start_st = 0;
	vector<int> seed_gen = {0,1,1,0};
	vector<double> rule_values = {0.4, 0.6, 0.4, 0.7, 0.4, 0.7, 0.7, 0.6};
	initialise_seed_grid(grid_size, seed_gen);
	initialise_rule(rule_values);
	initialise_state(grid_size);
	preprocess_probability(grid_size);
	start_st = start_state(seed_gen);
	binary_exponentiation(grid_size,start_st,generation);
	vector<pair<double,int>> pi(total_states);
	cout<<"Start State= "<<start_st<<endl;
	cout<<"Probability from start state:\n";
	for(int i=0;i<total_states; ++i){
		cout<<start_st<<" to "<<i<<" => "<<prob_k[start_st][i]<<"\n";
		pi[i] = {prob_k[start_st][i], i};
	}
	sort(pi.begin(), pi.end(), greater<pair<double,int>>());
	cout<<"\n****************\n";
	cout<<"Transition Probability In Decreasing Order Of Their Values:\n";
	for(int i=0; i<total_states; ++i){
		cout<<start_st<<" to "<<pi[i].second<<" => "<<pi[i].first<<"\n";
	}
	cout<<"\n\nThus we can easily see that three most likely states are:\n";
	for(int i=0;i<3;++i){
		cout<<"State = "<<pi[i].second<<endl;
		cout<<"Configuration =\n";
		cout<<"|";
		for(auto el : state[pi[i].second]){
			cout<<"| "<<el<<" |"; 
		}	
		cout<<"|"<<endl<<endl;
	}

	return 0;
	//print();

}
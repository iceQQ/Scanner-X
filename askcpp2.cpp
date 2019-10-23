#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iomanip>
#include <sstream>
#define n 248

using namespace std;

int main() {
	string countries[n];
	string abr[n];
	long pop[n][57];
	string line,word;
	fstream fin;
	fin.open("population-figures-easy.csv",ios::in);
	getline(fin,line);
	int i;
	i=0;
	while(getline(fin,line)){
		stringstream ss(line);
		int k=0;
		while(getline(ss,word,',')){
			if(k==0){
				countries[i]=word;
			}
			else if (k==1){
				abr[i]=word;
			}

			else{
				pop[i][k] = atol(word.c_str());
			}
			k++;
		}
		i++;
	}
	fin.close();
	int j,av=0,ac=0;
	float maxdif;
    for(i=1;i<n;i++){
        maxdif = (float)(pop[i][0]+pop[i][1])/(pop[i][0])*100;
        for(j=0;j<56;j++){
            if (maxdif < (float)(pop[i][j]+pop[i][j+1])/(pop[i][j])*100){
                maxdif = (float)(pop[i][j]+pop[i][j+1])/(pop[i][j])*100;
                av=1960+j;
                ac=1960+j+1;
            }
        }
        cout << fixed;
        cout << setprecision(2);
        cout << countries[i] << " " << abr[i] << " " <<  av << "-" << ac << " --> " << maxdif << "%" << endl;
        cout <<  "--------------------------------------------------------" << endl;

    }
	return 0;
}

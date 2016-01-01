// this code is my answer of query board question
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
    	if(!item.empty()){
    		elems.push_back(item);
    	}
    }
    return elems;
}

std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, elems);
    return elems;
}

int _data[256][256];

void _decode(std::string line){
	std::vector<std::string> _line = split(line, ' ');
	std::transform(_line[0].begin(), _line[0].end(), _line[0].begin(), ::tolower);
	int i;
	if(_line.size()==2){
		int temp1;
		stringstream ss(_line[1]);
		ss >> temp1;
		std::size_t sum = 0;
		if(_line[0]=="querycol"){
			for(i=0;i<256;i++){
				sum += _data[temp1][i];
			}
		}
		if(_line[0]=="queryrow"){
			for(i=0;i<256;i++){
				sum += _data[i][temp1];
			}
		}
		cout<<sum<<endl;
	}else if(_line.size()==3){
		int temp1, temp2;
		stringstream ss(_line[1]);
		ss >> temp1;
		stringstream ss2(_line[2]);
		ss2 >> temp2;
		if(_line[0]=="setcol"){
			for(i=0;i<256;i++){
				_data[temp1][i] = temp2;
			}
		}
		if(_line[0]=="setrow"){
			for(i=0;i<256;i++){
				_data[i][temp1] = temp2;
			}
		}
	}
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;

    while (getline(stream, line)) {
        // Do something with the line
        // if there is a newline
        if(line[line.length()-1]=='\n'){
        	line.pop_back();
        }

        _decode(line);
    }
    return 0;
}

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int num, i = 0;
std::vector<std::string> _data;
std::vector<int> len;

void _decode(std::string line){
	if(i<num){
		_data.push_back(line);
		len.push_back(line.length());
	}else{
		int m, min = len[0], idx;
		for(m=0;m<num;m++){
			if(min>len[m]){
				min = len[m];
				idx = m;
			}
		}
		_data[idx] = line;
		len[idx] = line.length();
	}
	i++;
}

void _sort(void){
	int k, l;
	for(k=0;k<num-1;k++){
		for(l=num-1;l>k;l--){
			if(len[l-1]<len[l]){
				std::string temp;
				temp = _data[l];
				_data[l] = _data[l-1];
				_data[l-1] = temp;

				std::size_t temp1 = len[l-1];
				len[l-1] = len[l];
				len[l] = temp1;
			}
		}
	}
	for(k=0;k<num;k++){
		cout<<_data[k]<<endl;
	}
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    std::size_t n = 1;
    while (getline(stream, line)) {
        // Do something with the line
        // if there is a newline
        if(line[line.length()-1]=='\n'){
        	line.pop_back();
        }
        if(n==1){
        	stringstream xx(line);
        	xx >> num;
        	n = 0;
        }else{
        	_decode(line);
        }
    }
    _sort();
    return 0;
}

#include <iostream>
#include <string>
#include <list>
using namespace std;

int main(){
    string test = "Hello World";
    cout<<test<<endl;
    int length = size(test);
    cout<<length<<endl;
    char partOfTest = test[0];
    cout<<partOfTest<<endl;
    cout<<endl;
    list<int> numbers = {1,2,3,4};
    list<string> stringNumbers = {"1","2","3","4"};
    list<string> stringList = {"name","age","birthday"};
    list<string> emptyList = {};
    list<int> numberList;
    for(int i=1;i<5;i++){
        numberList.push_back(i);
    }
    list<int> forSorting = {3,10,9,8,1};
    forSorting.sort();
    for(int i:numbers){
        cout<<i<<" ";
    }
    cout<<endl;

    for(string i:stringList){
        cout<<i<<" ";
    }
    cout<<endl;

    for(string i:emptyList){
        cout<<i<<" ";
    }
    cout<<endl;
    for(int i:numberList){
        cout<<i<<" ";
    }
    cout<<endl;
    for(int i:numbers){
        cout<<i<<" ";
    }
    for(string i:stringList){
        cout<<i<<" ";
    }
    cout<<endl;

    for(int i:forSorting){
        cout<<i<<" ";
    }
    cout<<endl;
    
    if(numbers.size() == numberList.size()){
        cout<<"True"<<endl;
    } else {
        cout<<"False"<<endl;
    }
    cout<<forSorting.size()<<endl;
}

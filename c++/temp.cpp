// #include <iostream>
// #include <string>
// using namespace std;

// void checkstring(string str)
// {
//     for (char &ch : str)
//     {
//         if (isalpha(ch))
//         {
//             if (islower(ch))
//             {
//                 ch = toupper(ch);
//             }

//             else if (isupper(ch))
//             {
//                 ch = tolower(ch);
//             }
//         }
//     }
//         cout<<str;
// };

// int main()
// {
//     string str;
//     cin >> str;
//     checkstring(str);
//     return 0;
// }

// #include<iostream>
// using namespace std;

// int main(){
//     string str = "sdjkdhfei";
//     int count = 0;

//     for(int i = 0; i < str.size(); i++){
//         if(str[i] == 'k'){
//             count++;
//         }
//     }
//     cout<<count<<endl;
    
//     return 0;
// }




#include<iostream>
#include<string>
using namespace std;

void reverseString(string str){
    int i = 0;
    int j = str.size() - 1;
    while(i <= j){
        swap(str[i],str[j]);
        i++;
        j--;
    }
    cout<<str<<endl;
}

int main(){
    string str;
    cin>>str;
    reverseString(str);
    return 0;
}
//using namespace std;

/*IGNORE THE WARNINGS AND ERRORS BECAUSE ON LOCAL YOU PROBABLY DOESN'T HAVE SAME 
LISTNODE OR OTHER BASE STRUCTURE WITH LEETCODE PROBLEMS SO THATS NOT A PROBLEM*/

class Solution {
public:
     int nthUglyNumber(int n) {
          int res = 0;
          vector<int> res_ls(n);
          res_ls[0] = 1;
          if (1 <= n | n <=1690)
          {
               if (n == 1)
               {
                    return 1;
               }
               else if (n != 1)
               {
                    int p1 = 0;
                    int p2 = 0;
                    int p3 = 0;
                    for (int i = 1; i < n; i++)
                    {
                         int twoMul = res_ls[p1] * 2;
                         int threeMul = res_ls[p2] * 3;
                         int fiveMul = res_ls[p3] * 5;
                         res_ls[i] = min(twoMul, min(threeMul,fiveMul ));

                         if(res_ls[i] == twoMul) p1++;
                         if(res_ls[i] == threeMul) p2++;
                         if(res_ls[i] ==  fiveMul) p3++;
                    }
               }
          }
          else
          {
               cout << "None" << endl;
          }
          return res_ls[n - 1];
     }
    
};
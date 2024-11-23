
/*IGNORE THE WARNINGS AND ERRORS BECAUSE ON LOCAL YOU PROBABLY DOESN'T HAVE SAME 
LISTNODE OR OTHER BASE STRUCTURE WITH LEETCODE PROBLEMS SO THATS NOT A PROBLEM*/

class Solution {
public:
     ListNode* sortList(ListNode* head) 
     {
          vector<int> insert;
          ListNode* temp = head;
          while(temp != NULL)
          {
               insert.push_back(temp->val);
               temp = temp->next;
          }
          temp = head;
          sort(insert.begin(), insert.end());
          int i = 0;
          while(temp != NULL && i < insert.size())
          {
               temp->val = insert[i];
               i++;
               temp = temp->next;

          }
          return head;
     }
};
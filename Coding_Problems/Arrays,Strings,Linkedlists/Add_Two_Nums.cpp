#include<iostream>
using namespace std;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy=new ListNode(0);
        ListNode* curr = dummy;
        int carry =0;
        
        while(l1!=NULL || l2!=NULL || carry!=0){
            int v1 = l1 ? l1->val :0;
            int v2 =l2 ? l2->val :0;
            
            
            int value = v1+v2 +carry;
            carry =value / 10;
            value = value % 10;
            
            //update the pointers
            curr->next=new ListNode(value);
            curr=curr->next;
            
            l1=l1 ? l1->next :nullptr;
            l2=l2 ? l2->next :nullptr;
            
            
        }
        
        return dummy->next;
        
    }
};
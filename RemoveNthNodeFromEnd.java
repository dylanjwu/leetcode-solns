 /* Definition for singly-linked list.*/
  public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }
 
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode curr = head;
        int len = 0;
        while(curr != null){
            curr = curr.next;
            len++;
        }
        
        curr = dummy;
        int index = len-n;
        int i = 0;
        ListNode prev = null;
        while(i < index){
            curr = curr.next;
            prev = curr;
            i++;
        }
        curr.next = curr.next.next;
        return dummy.next;
    }
}
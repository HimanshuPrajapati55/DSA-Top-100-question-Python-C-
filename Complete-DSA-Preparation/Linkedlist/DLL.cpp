#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node* prev;

    Node(int data1, Node* next1 = nullptr, Node* prev1 = nullptr) {
        data = data1;
        next = next1;
        prev = prev1;
    }
};

Node* convertArr2DLL(vector<int> &arr) {
    if (arr.empty()) return nullptr; // Handle empty array case

    Node* head = new Node(arr[0]);
    Node* prev = head;

    for (int i = 1; i < arr.size(); i++) {
        Node* temp = new Node(arr[i], nullptr, prev);
        prev->next = temp;
        prev = temp;
    }

    return head;
}
void print(Node* head) {
    while (head != nullptr) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

Node* deleteHead(Node* head){
    if(head == NULL || head -> next == NULL){
        return NULL;

    }
    Node* prev = head;
    head = head-> next;

    head->prev = nullptr;
    prev->next = nullptr;

    delete prev;
    return head;

}

Node* deletetail(Node* head){
    if(head == NULL || head -> next == NULL){
        return NULL;

    }
    Node* tail = head;
    while(tail -> next != NULL){
        tail = tail -> next;
    }
    Node* newTail = tail -> prev;
    newTail -> next  = nullptr;
    tail -> prev = nullptr;
    delete tail;
    return head; 
}

Node* deleteKth(Node* head, int k){
    if(head == NULL){
        return NULL;
    }
    int cnt = 0;
    Node* Knode = head;
    while(Knode != NULL){
        cnt++;
        if(cnt == k) break;
        Knode = Knode -> next;
    }
    Node* prev = Knode -> prev;
    Node* front = Knode -> next;

    if(prev == NULL && front == NULL){
        return NULL;
    }
    else if(prev == NULL){
        return deleteHead(head);
    }
    else if(front == NULL)
    {
        return deleteHead(head);
    }
    prev -> next = front;
    front -> prev = prev;

    Knode-> next = nullptr;
    Knode-> prev = nullptr;
    delete Knode;
    return head;
    
    
}



int main() {
    vector<int> arr = {12, 5, 8, 7};
    Node* head = convertArr2DLL(arr);
    head = deleteKth(head, 2);
    print(head); // Call the print function to display the list
    return 0;
}
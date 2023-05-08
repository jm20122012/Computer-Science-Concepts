import Node from './ListNode.js';

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    prepend(data) {
        const node = new Node(data);

        // If the list is empty, make the new node the head and tail
        if (this.head === null) {
            this.head = node;
            this.tail = node;
        }
        // Otherwise, add the new node to the beginning of the list
        else {
            node.next = this.head;
            this.head = node;           
        }
 
    }
    
    append(data) {
        const node = new Node(data);
        // If the list is empty, make the new node the head and tail
        if (this.head === null) {
            this.head = node;
            this.tail = node;
        }
        // Otherwise, add the new node to the end of the list
        else {
            this.tail.next = node;
            this.tail = node;
        }
    }

    printHead() {
        console.log("Head: ", this.head);
    }

    printTail() {
        console.log("Tail: ", this.tail);
    }

}

const list = new LinkedList();
list.prepend(0);

const min = 1;
const max = 100;

for (let i = 0; i < 20; i++) {
    const randomInt = Math.floor(Math.random() * (max - min + 1)) + min;
    list.append(randomInt);
}

list.printHead();
list.printTail();

list.prepend(100);

list.printHead();
list.printTail();


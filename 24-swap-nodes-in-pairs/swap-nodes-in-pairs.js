const swapPairs = function (head) {
    let dummy = { val: 0, next: head };
    let current = dummy;

    while (current.next && current.next.next) {
        let first = current.next;
        let second = first.next;

        
        first.next = second.next;
        second.next = first;
        current.next = second;

        
        current = first;
    }

    return dummy.next;
};

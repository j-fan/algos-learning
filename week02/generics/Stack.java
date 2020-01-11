import java.util.Iterator;

public class Stack<Item> implements Iterable<Item> {
    private Node first = null;

    private class Node {
        Item item;
        Node next;
    }

    public Iterator<Item> iterator() {
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext() {
            return current != null;
        }

        public Item next() {
            Item item = current.item;
            current = current.next;
            return item;
        }

        public void remove() {
            throw Exception("Remove() iterator is not supported");
        }
    }

    public boolean isEmpty() {
        return first == null;
    }

    public void push(Item item) {
        Node oldFirst = first;

        first = new Node();
        first.item = item;

        first.next = oldFirst;
    }

    public Item pop() {
        Node oldFirst = first;
        first = oldFirst.next;

        oldFirst.next = null;

        return oldFirst.item;
    }

    public void show() {
        Iterator<Item> it = iterator();
        while (it.hasNext()) {
            System.out.print(it.next() + ", ");
        }
        System.out.println();
    }
}
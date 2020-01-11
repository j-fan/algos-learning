class Generics {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<String>();
        stack.push("item1");
        stack.push("item2");
        stack.push("item3");
        stack.push("item4");
        stack.push("item5");
        stack.show();
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        for (String s : stack) {
            System.out.print(s + ",");
        }
        System.out.println();
    }
}
using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;

public class Node
{
    public int key;
    public int val;
    public Node? left;
    public Node?right;

    public Node(int key, int val)
    {
        this.key = key;
        this.val = val;
    }
}

public class TreeMap
{

    public Node? root = null;

    public void Insert(int key, int val)
    {
        Node newNode = new Node(key, val);

        if (root == null)
        {
            root = newNode;
            return;
        }

        Node curr = root;
        while (curr is not null)
        {
            if (key < curr.key)
            {
                if (curr.left == null)
                {
                    curr.left = newNode;
                    return;
                }
                curr = curr.left;
            }
            else if (key > curr.key)
            {
                if (curr.right == null)
                {
                    curr.right = newNode;
                    return;
                }
                curr = curr.right;
            }
            else
            {
                curr.val = val;
            }
        }
    }

    // dfs
    public void InOrderTraversal()
    {
        void InOrder(Node curr)
        {
            if (curr == null) return;
            
            InOrder(curr.left);
            Console.WriteLine(curr.val);
            InOrder(curr.right);
        }
        InOrder(root);
    }
    
    public void InOrderTraversalIter()
    {
        Stack<Node> stack = new Stack<Node>();
        Node curr = root;

        while (curr is not null || stack.Count > 0)
        {
            while (curr is not null)
            {
                stack.Push(curr);
                curr = curr.left;
            }

            curr = stack.Pop();
            Console.WriteLine(curr.val);
            
            curr = curr.right;
        }
    }

    public void BFS()
    {
        Queue<Node> queue = new Queue<Node>();

        Node curr = root;
        queue.Enqueue(curr);

        while (queue.Count != 0)
        {
            curr = queue.Dequeue();
            if (curr.left is not null)
            {
                queue.Enqueue(curr.left);
            }

            Console.WriteLine(curr.val);

            if (curr.right is not null)
            {
                queue.Enqueue(curr.right);
            }
        }
    }
}



class Program
{
    public static void Main()
    {
        TreeMap treeMap = new TreeMap();
        treeMap.Insert(2, 2);
        treeMap.Insert(1, 1);
        treeMap.Insert(3, 3);

        Console.WriteLine(treeMap.root.left.val);
        Console.WriteLine(treeMap.root.val);
        Console.WriteLine(treeMap.root.right.val);
        
        Console.WriteLine("-");
        treeMap.InOrderTraversal();
        Console.WriteLine("-");
        treeMap.InOrderTraversalIter();

    }
}

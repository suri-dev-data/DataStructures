<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Structures in Python</title>
</head>
<body>

<h1>Data Structures in Python</h1>

<p>Repository with implementations of fundamental data structures in Python. These structures are the backbone of many algorithms and are essential in solving complex problems efficiently. Below is a list of the data structures implemented, with a brief summary and usage examples.</p>

<h3>1. Stack</h3>
<p>A Stack is a linear data structure that follows the <strong>Last In, First Out (LIFO)</strong> principle. Elements can only be added or removed from the top of the stack.</p>

<h4>Methods:</h4>
<ul>
    <li><code>push</code>: Add an item to the top of the stack.</li>
    <li><code>pop</code>: Remove and return the top item from the stack.</li>
    <li><code>peek</code>: Get the top item without removing it.</li>
    <li><code>is_empty</code>: Check if the stack is empty.</li>
    <li><code>size</code>: Return the number of elements in the stack.</li>
    <li><code>clear</code>: Empty the stack.</li>
</ul>

<h3>2. Queue</h3>
<p>A Queue is a linear data structure that follows the <strong>First In, First Out (FIFO)</strong> principle. Elements are added at the rear and removed from the front.</p>

<h4>Methods:</h4>
<ul>
    <li><code>enqueue</code>: Add an item to the rear of the queue.</li>
    <li><code>dequeue</code>: Remove and return the front item from the queue.</li>
    <li><code>peek</code>: Get the front item without removing it.</li>

</ul>

<h3>3. Linked List</h3>
<p>A Linked List is a linear data structure where each element (node) contains a reference (pointer) to the next node in the sequence. It allows efficient insertion and deletion of elements.</p>

<h4>Types:</h4>
<ul>
    <li><strong>Singly Linked List</strong>: Each node points to the next node.</li>
    <li><strong>Doubly Linked List</strong>: Each node points to both the next and the previous node.</li>
</ul>

<h4>Methods (Singly Linked List):</h4>
<ul>
    <li><code>add_first</code>: Add an item at the beginning of the list.</li>
    <li><code>add_last</code>: Add an item at the end of the list.</li>
    <li><code>remove_first</code>: Remove and return the first item from the list.</li>
    <li><code>remove_last</code>: Remove and return the last item from the list.</li>
    <li><code>find</code>: Search for an item in the list.</li>
</ul>

<h3>4. Binary Search Tree (BST)</h3>
<p>A Binary Search Tree is a hierarchical data structure where each node has at most two children. For each node, the left subtree contains values smaller than the node, and the right subtree contains values larger than the node.</p>

<h4>Methods:</h4>
<ul>
    <li><code>insert</code>: Insert an item into the BST.</li>
    <li><code>find</code>: Check if an item exists in the BST.</li>
    <li><code>delete</code>: Remove an item from the BST.</li>
    <li><code>inorder_traversal</code>: Traverse the tree in sorted order.</li>
</ul>

<h3>5. Hash Table</h3>
<p>A Hash Table is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array of buckets, from which the desired value can be found.</p>

<h4>Methods:</h4>
<ul>
    <li><code>put</code>: Insert or update a key-value pair.</li>
    <li><code>get(</code>: Retrieve the value associated with a key.</li>
    <li><code>remove</code>: Remove a key-value pair.</li>
    <li><code>contains_key</code>: Check if a key exists in the table.</li>
</ul>



</body>
</html>

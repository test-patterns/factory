# factory
Sample problem featuring the factory pattern.

Use the factory pattern when you want a method to return several possible classes that share a common super class.

# Class problem
Welcome to Pizza<sup>2</sup>! Our kitchen already outputs messages when a new Pizza or Calzone is ordered. See for yourself by running the following command:

```
python3 __main__.py -t P
```

```
python3 __main__.py -t C
```

Our chef wants to add a new item to the menu... Stromboli!! Using the factory design pattern, add the Stromboli dish to the menu by outputting messages when a Stromboli is ordered!

### UML

![alt text](http://yuml.me/b723c80f.png)
[edit](http://yuml.me/edit/b723c80f)

### Previous output

```
large pizza is being made
pizza is being cooked
pizza is being boxed

small calzone is being made
calzone is being cooked
calzone is being boxed
```

# Desired output

```
medium stromboli is being made
stromboli is being cooked
stromboli is being boxed
```

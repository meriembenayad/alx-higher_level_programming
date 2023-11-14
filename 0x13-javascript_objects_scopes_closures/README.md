## JavaScript - Objects, Scopes and Closures

### Resources

**Read or watch**:

- [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
- [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)**(read all examples!)**
- [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
- [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
- [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
- [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
- [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [this/self](https://alistapart.com/article/getoutbindingsituations/)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

### Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:

#### General

- Why JavaScript programming is amazing
- How to create an object in JavaScript- What `this` means
- What `undefined` means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

#### Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

### Requirements

#### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

### More Info

#### Install Node 14

```shell
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Install semi-standard

[Documentation](https://github.com/standard/semistandard)

```shell
$ sudo npm install semistandard --global
```

### Tasks
<details>
<summary>0. Rectangle #0</summary>

Write an empty class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class

```shell
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$ 
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `0-rectangle.js`
</details>

<details>
<summary>1. Rectangle #1</summary>

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`

```shell
guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `1-rectangle.js`
</details>

<details>
<summary>2. Rectangle #2</summary>

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object

```shell
guillaume@ubuntu:~/0x13$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$ 
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `2-rectangle.js`
</details>

<details>
<summary>3. Rectangle #3</summary>

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments: `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object
- Create an instance method called `print()` that prints the rectangle using the character `X`

```shell
guillaume@ubuntu:~/0x13$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
guillaume@ubuntu:~/0x13$ 
```
***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `3-rectangle.js`
</details>

<details>
<summary>4. Rectangle #4</summary>

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments: `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object
- Create an instance method called `print()` that prints the rectangle using the character `X`
- Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
- Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2

```shell
guillaume@ubuntu:~/0x13$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

guillaume@ubuntu:~/0x13$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x13$ 
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `4-rectangle.js`
</details>

<details>
<summary>5. Square #0</summary>

Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:

- You must use the `class` notation for defining your class and `extends`
- The constructor must take 1 argument: `size`
- The constructor of `Rectangle` must be called (by using `super()`)

```shell
guillaume@ubuntu:~/0x13$ cat 5-main.js
#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

guillaume@ubuntu:~/0x13$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
guillaume@ubuntu:~/0x13$
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `5-square.js`
</details>

<details>
<summary>6. Square #1</summary>

Write a class `Square` that defines a square and inherits from `Square` of `5-square.js`:

- You must use the `class` notation for defining your class and `extends`
- Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
    - If `c` is `undefined`, use the character `X`

```shell
guillaume@ubuntu:~/0x13$ cat 6-main.js
#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

guillaume@ubuntu:~/0x13$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
guillaume@ubuntu:~/0x13$ 
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `6-square.js`
</details>

<details>
<summary>7. Occurrences</summary>

Write a function that returns the number of occurrences in a list:

- Prototype: `exports.nbOccurences = function (list, searchElement)`

```shell
guillaume@ubuntu:~/0x13$ cat 7-main.js
#!/usr/bin/node
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));

guillaume@ubuntu:~/0x13$ ./7-main.js
1
4
2
guillaume@ubuntu:~/0x13$ 
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `7-occurrences.js`
</details>

<details>
<summary>8. Esrever</summary>

Write a function that returns the reversed version of a list:

- Prototype: `exports.esrever = function (list)`
- You are not allow to use the built-in method `reverse`

```shell
guillaume@ubuntu:~/0x13$ cat 8-main.js
#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(["School", 89, { id: 12 }, "String"]));

guillaume@ubuntu:~/0x13$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'School' ]
guillaume@ubuntu:~/0x13$
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `8-esrever.js`
</details>

<details>
<summary>9. Log me</summary>

Write a function that prints the number of arguments already printed and the new argument value. (see example below)

- Prototype: `exports.logMe = function (item)`
- Output format: `<number arguments already printed>: <current argument value>`

```shell
guillaume@ubuntu:~/0x13$ cat 9-main.js
#!/usr/bin/node
const logMe = require('./9-logme').logMe;

logMe("Hello");
logMe("Best");
logMe("School");

guillaume@ubuntu:~/0x13$ ./9-main.js
0: Hello
1: Best
2: School
guillaume@ubuntu:~/0x13$
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `9-logme.js`
</details>

<details>
<summary>10. Number conversion</summary>

Write a function that converts a number from base 10 to another base passed as argument:

- Prototype: `exports.converter = function (base)`
- You are not allowed to import any file
- You are not allowed to declare any new variable (`var`, `let`, etc..)

```shell
guillaume@ubuntu:~/0x13$ cat 10-main.js
#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

guillaume@ubuntu:~/0x13$ ./10-main.js
2
12
89
2
c
59
guillaume@ubuntu:~/0x13$ 
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `10-converter.js`
</details>

<details>
<summary>11. Factor index</summary>

Write a script that imports an array and computes a new array.

- Your script must import `list` from the file `100-data.js`
- You must use a `map`. [Tips](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map?v=control)
- A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
- Print both the initial list and the new list

```shell
guillaume@ubuntu:~/0x13$ cat 100-data.js
#!/usr/bin/node
exports.list = [1, 2, 3, 4, 5];
guillaume@ubuntu:~/0x13$ ./100-map.js 
[ 1, 2, 3, 4, 5 ]
[ 0, 2, 6, 12, 20 ]
guillaume@ubuntu:~/0x13$ 
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `11-second_biggest.js`
</details>

<details>
<summary>12. Object</summary>

Update this script to replace the value `12` with `89`:

- You are not allowed to use `var`

```shell
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `12-object.js`
</details>

<details>
<summary>13. Add file</summary>

Write a function that returns the addition of 2 integers.

- The function must be visible from outside
- The name of the function must be `add`
- You are not allowed to use `var`

[Tip](https://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)

```shell
guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `13-add.js`
</details>

<details>
<summary>14. Const or not const</summary>

Write a file that modifies the value of `myVar` to `333`

```shell
guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$ 
```

![Hell Yeah](hell_yeah.jpeg)

Do you get it? Tweet! Post! Talk about it!

Hint: Scope

**This exercise doesn’t pass `semistandard`** so don’t worry about it.

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `100-let_me_const.js`
</details>

<details>
<summary>15. Call me Moby</summary>

Write a function that executes `x` times a function.

- The function must be visible from outside
- Prototype: `function (x, theFunction)`
- You are not allowed to use `var`

```shell
guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ 
```

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `101-call_me_moby.js`
</details>


<details>
<summary></summary>

***
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x13-javascript_objects_scopes_closures`
- File: `0-javascript_is_amazing.js`
</details>

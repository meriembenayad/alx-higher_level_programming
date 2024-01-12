## JavaScript - Web JQuery

#### Concepts

_For this project, we expect you to look at these concepts:_

- [JavaScript in the browser](javascript_in_browser.md)
- [Dealing with data statically versus dynamically](https://intranet.alxswe.com/concepts/35)

### Resources

**Read or watch**:

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
- [Get and set content](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
- [Manipulate CSS classes](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
- [Manipulate DOM elements](https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)
- [API](https://oscarotero.com/jquery/)
- [Introduction To Ajax](https://jquery-tutorial.net/ajax/introduction/)
- [GET & POST request](https://jquery-tutorial.net/ajax/the-get-and-post-methods/)
- [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
- [JQuery](https://jquery.com/)
- [JQuery API](https://api.jquery.com/)
- [JQuery Ajax](https://learn.jquery.com/ajax/)

### More Info

#### Import JQuery

```shell
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

### Tasks:


<details>
<summary>0. No JQuery</summary>

Write a JavaScript script that alters the text color of the `<header>` element to red (`#FF0000`):

- You are required to use `document.querySelector` to select the HTML tag
- The JQuery API is not allowed for this task

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```
***
- File: `0-script.js`
</details>

<details>
<summary>1. With JQuery</summary>

Write a JavaScript script that changes the text color of the `<header>` element to red (`#FF0000`):

- You are not allowed to use `document.querySelector` to select the HTML tag
- You are required to use the JQuery API

Please verify with this HTML file in your web browser:

```shell
guillaume@ubuntu:~/0x15$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `1-script.js`
</details>

<details>
<summary>2. Click and turn red</summary>

Develop a JavaScript script that modifies the text color of the `<header>` element to red (`#FF0000`) upon the user clicking on the `DIV#red_header` tag:

- The use of `document.querySelector` to select the HTML tag is prohibited
- The JQuery API must be utilized.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `2-script.js`
</details>

<details>
<summary>3. Add `.red` class</summary>

Compose a JavaScript script that appends the class `red` to the `<header>` element when the user interacts with the `DIV#red_header` tag by clicking on it:

- The use of `document.querySelector` to select the HTML tag is not permitted
- The JQuery API is required to be used.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `3-script.js`
</details>

<details>
<summary>4. Toggle classes</summary>

Develop a JavaScript script that switches the class of the `<header>` element each time the user interacts with the `DIV#toggle_header` tag by clicking on it:

- The `<header>` element should always have a single class: either `red` or `green`, but never both simultaneously and never none.
- If the existing class is `red`, when the user clicks on `DIV#toggle_header`, the class should be changed to `green` and vice versa.
- The use of `document.querySelector` to select the HTML tag is not allowed.
- The JQuery API must be utilized.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `4-script.js`
</details>

<details>
<summary>5. List of elements</summary>

Craft a JavaScript script that appends a `<li>` element to a list each time the user interacts with the `DIV#add_item` tag by clicking on it:

- The new element should be: `<li>Item</li>`
- The new element should be inserted into `UL.my_list`
- The use of `document.querySelector` to select the HTML tag is not permitted
- The JQuery API must be utilized.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `5-script.js`
</details>

<details>
<summary>6. Change the text</summary>

Develop a JavaScript script that modifies the text of the `<header>` element to `New Header!!!` when the user interacts with the `DIV#update_header` tag by clicking on it:

- The use of `document.querySelector` to select the HTML tag is not allowed
- The JQuery API must be utilized.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `6-script.js`
</details>

<details>
<summary>7. Star wars character</summary>

Compose a JavaScript script that retrieves the character `name` from this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`

- The name should be presented in the HTML tag `DIV#character`
- The use of `document.querySelector` to select the HTML tag is not permitted
- The JQuery API must be utilized.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `7-script.js`
</details>

<details>
<summary>8. Star Wars movies</summary>

Develop a JavaScript script that retrieves and enumerates the `title` for all movies by utilizing this URL: `https://swapi-api.alx-tools.com/api/films/?format=json`

- All movie titles should be listed in the HTML tag `UL#list_movies`
- The use of `document.querySelector` to select the HTML tag is not allowed
- The JQuery API must be utilized.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `8-script.js`
</details>

<details>
<summary>9. Say Hello!</summary>

Compose a JavaScript script that retrieves from `https://hellosalut.stefanbohacek.dev/?lang=fr` and presents the value of `hello` from that fetch in the HTML tag `DIV#hello`.

- The translated version of “hello” should be displayed in the HTML tag `DIV#hello`
- The use of `document.querySelector` to select the HTML tag is not permitted
- The JQuery API must be utilized
- Your script should function correctly when it is imported from the `<head>` tag.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `9-script.js`
</details>

<details>
<summary>10. No jQuery - document loaded</summary>

Develop a JavaScript script that modifies the text color of the `<header>` element to red (`#FF0000`):

- You are required to use `document.querySelector` to select the HTML tag
- The use of the jQuery API is not permitted
- Please note: Your script should be imported from the `<head>` tag, not at the end of the HTML.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 100-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `100-script.js`
</details>

<details>
<summary>11. List, add, remove</summary>

Develop a JavaScript script that performs the following actions on `LI` elements in a list when the user clicks:

- The new element should be: `<li>Item</li>`
- The new element should be appended to `UL.my_list`
- When the user interacts with `DIV#add_item` by clicking on it, a new element is added to the list
- When the user interacts with `DIV#remove_item` by clicking on it, the last element is removed from the list
- When the user interacts with `DIV#clear_list` by clicking on it, all elements in the list are cleared
- The use of `document.querySelector` to select the HTML tag is not permitted
- The JQuery API must be utilized
- Your script should function correctly when it is imported from the `HEAD` tag.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 101-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `101-script.js`
</details>

<details>
<summary>12. Say hello to everybody!</summary>

Develop a JavaScript script that retrieves and displays the translation of "Hello" in the specified language:

- You are required to use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
- The language code will be the value inputted in the tag `INPUT#language_code` (examples: `es`, `fr`, `en` etc.)
- The translation should be fetched when the user interacts with `INPUT#btn_translate` by clicking on it
- The translated version of "Hello" should be presented in the HTML tag `DIV#hello`
- The use of `document.querySelector` to select the HTML tag is not permitted
- The JQuery API must be utilized
- Your script should function correctly when it is imported from the `<head>` tag.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 102-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `102-script.js`
</details>

<details>
<summary>13. And press ENTER</summary>

Develop a JavaScript script that retrieves and displays the translation of "Hello" in the specified language:

- You are required to use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
- The language code will be the value inputted in the tag `INPUT#language_code` (examples: `es`, `fr`, `en` etc.)
- The translation should be fetched when the user interacts with `INPUT#btn_translate` by clicking on it OR presses `ENTER` when `INPUT#language_code` is in focus
- The translated version of "Hello" should be presented in the HTML tag `DIV#hello`
- The use of `document.querySelector` to select the HTML tag is not permitted
- The JQuery API must be utilized
- Your script should function correctly when it is imported from the `<head>` tag.

Please test with this HTML file in your browser:

```shell
guillaume@ubuntu:~/0x15$ cat 103-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

***
- File: `103-script.js`
</details>

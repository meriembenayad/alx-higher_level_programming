## JavaScript - Web scraping

### Resources

**Read or watch**:

- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [request module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

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

#### Install `request` module and use it

[Documentation](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ "Documentation")

```shell
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

**Notes:** Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

### Tasks

<details>
<summary>0. Readme</summary>

Create a script that loads and displays the contents of a file.

- The file path should be provided as the first argument
- The file's content should be loaded using the `utf-8` encoding
- If there's an error while loading the file, the error object should be printed out.

```shell
guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$
```
***
**File:**

- File: `0-readme.js`
</details>

<details>
<summary>1. Write me</summary>

Develop a script that records a string into a file.

- The first argument should be the file path
- The second argument should be the string to be recorded
- The file's content should be written using the `utf-8` encoding
- If an error arises during the writing process, the error object should be displayed.

```shell
guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$
```
***
**File:**
- File: `1-writeme.js`
</details>

<details>
<summary>2. Status code</summary>

Create a script that shows the status code of a `GET` request.

- The first argument should be the URL to be requested (`GET`)
- The status code should be displayed in this format: `code: <status code>`
- The `request` module must be utilized for this task.

```shell
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$ 
```
***
**File:**
- File: `2-statuscode.js`
</details>

<details>
<summary>3. Star wars movie title</summary>

Develop a script that outputs the title of a Star Wars film corresponding to a specific episode number.

- The first argument should be the movie ID
- You need to use the [Star Wars API](https://swapi-api.alx-tools.com/) with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`
- The `request` module must be used for this task.

```shell
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
guillaume@ubuntu:~/0x14$ 
```
***
**File:**
- File: `3-starwars_title.js`
</details>

<details>
<summary>4. Star wars Wedge Antilles</summary>

Develop a script that outputs the count of films featuring the character "Wedge Antilles".

- The first argument should be the API URL of the [Star Wars API](https://swapi-api.alx-tools.com/): `https://swapi-api.alx-tools.com/api/films/`
- "Wedge Antilles" is identified by the ID `18` - your script **must** use this ID to filter the API's result
- The `request` module must be used for this task.

```shell
guillaume@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
guillaume@ubuntu:~/0x14$ 
```
***
**File:**
- File: `4-starwars_count.js`
</details>

<details>
<summary>5. Loripsum</summary>

Develop a script that retrieves the contents of a webpage and saves it in a file.

- The first argument should be the URL to be requested
- The second argument should be the file path where the body response will be stored
- The file should be encoded in UTF-8
- The `request` module must be used for this task.

```shell
guillaume@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
guillaume@ubuntu:~/0x14$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>

<p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>

<p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. </p>

<p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. </p>

guillaume@ubuntu:~/0x14$
```
***
**File:**
- File: `5-request_store.js`
</details>

<details>
<summary>6. How many completed?</summary>

Develop a script that calculates the count of tasks completed by each user id.

- The first argument should be the API URL: `https://jsonplaceholder.typicode.com/todos`
- Only users with completed tasks should be printed
- The `request` module must be used for this task.

```shell
guillaume@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
guillaume@ubuntu:~/0x14$
```
***
**File:**
- File: `6-completed_tasks.js`
</details>

<details>
<summary>7. Who was playing in this movie?</summary>

Develop a script that displays all characters from a specific Star Wars film:

- The first argument should be the Movie ID - for instance, `3` corresponds to “Return of the Jedi”
- Each character name should be printed on a separate line
- You need to use the [Star Wars API](https://swapi-api.alx-tools.com/)
- The `request` module must be used for this task.

```shell
guillaume@ubuntu:~/0x14$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
guillaume@ubuntu:~/0x14$ 
```
***
**File:**
- File: `100-starwars_characters.js`
</details>

<details>
<summary>8. Right order</summary>

Develop a script that displays all characters from a specific Star Wars film:

- The first argument should be the Movie ID - for instance, `3` corresponds to “Return of the Jedi”
- Each character name should be printed on a separate line, **following the same sequence as the "characters" list in the `/films/` response**
- You need to use the [Star Wars API](https://swapi-api.alx-tools.com/")
- The `request` module must be used for this task.

```shell
guillaume@ubuntu:~/0x14$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
guillaume@ubuntu:~/0x14$ 
```
***
**File:**
- File: `101-starwars_characters.js`
</details>

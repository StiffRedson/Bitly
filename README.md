# References reduction by means of bitli
___

This application reduces references or counts a number of transfers by the references with has already been reducted by this service  [bitly](https://bitly.com/)
## How to install?
---
* install python
  * in linux
  ```
  $ sudo apt install python3
  ```
  * in windows

  have to install [python.org](https://www.python.org/downloads/windows/) download and install

* install virtual environment

  * install pip3

  for linux

    ```
  $ sudo apt install python3-pip
    ```

  for windows

    ```
    pip

    ```

  * environment


  ```
  pip install -r requirements.txt
  ```

* get token on bit.li

This program has a limited resourse for references convertion
And you can use my token while downloading to your computer

 **TOKEN** - _is used for an owner identification for a safe remote access to information resources_

  * Register and get your token here [bitly](https://dev.bitly.com/get_started.html)
  * create a text file and compress the following strings

  >LOGIN=dvmn-tasks    
  >TOKEN=   __install your BITLY_TOKEN here__

  * Rename the text file into '.env'
  * Place this file into the project main folder

Ready!




## How to proceed?
---
The program is called out of a console.
Proceed to the program location and get started
Use the following reference as a function argument
```
$ python3 bitly.py -u http://bit.ly/20SouOG
[*] Number of clicks link: 10
```
The short reference shows a number of transfers
The long one will look like as at the console

## The Project Objective
---
The code is created for educational purposes on the website for web developers [dvmn.org](https://dvmn.org/modules/)

## Originator
---
| Contacts | Ivan Fedorov          |
|----------|-----------------------|
| Email    | StiffRedson@gmail.com |
| Telegram | @StivaRedson           |

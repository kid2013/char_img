# Research Project : Embedding-Generate Character JPGs 01

## Project Directories

* README.md -- doc : markdown about this project
* .gitignore -- doc: the ignore file for the git
* resources/ -- dir : directory to store resources
  + font_libs/ -- dir : directory to store font libs.
* outputs/ -- dir : directory to store the output jpgs.
  + chn/ -- dir : directory to store Chinese character jpgs, it can contain sub-directories.
  + eng/ -- dir : directory to store English character jpgs, it can contain sub-directories.
* emb_chars -- module : root module for the python program
  + chars -- module : sub module to get the chars list
  + jpgs -- module : sub module to generate jpgs for the given chars

## Git Command line instructions

### Git global setup

* git config --global user.name "abc"
* git config --global user.email "abc@cloudwalk.cn"

### Create a new repository

* git clone http://192.168.50.80/EMB/RS_CHR01.git
* cd RS_CHR01
* touch README.md
* git add README.md
* git commit -m "add README"
* git push -u origin master

### Existing folder or Git repository

* cd existing_folder
* git init
* git remote add origin http://192.168.50.80/EMB/RS_CHR01.git
* git add .
* git commit
* git push -u origin master
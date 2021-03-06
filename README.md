# Merged to https://github.com/ZackaryW/bitwarden-utils

# bitwarden-attachments-tool

> A Gui client is also available now
![image](https://user-images.githubusercontent.com/36378555/164945130-3ae45ec8-f0fd-40f2-ad27-b0343e9a9328.png)

> This repo is based on https://github.com/ckabalan/bitwarden-attachment-exporter

> Designed for personal use case but includes limited generic interfaces

> Script functions are accomplished using `Popen, Pipe` in subprocess, may introduce security vulnerabilities

# install 
```
pip install bw-util
```
> this tool requires bitwarden-cli to run

# Methods to run
## 1. in shell
```
bw-export [commands] [options]

# gui version as

bw-export-gui
```
## 2. (windows only) download release
at https://github.com/ZackaryW/bitwarden-attachments-tool/releases

# documentation

## base options
|option| description
|----|----|
pw      | password
session | sessionKey
savepath| export location
debug   | debug logging
apppath | specifies the location of bitwarden-cli

> it is also possible to set `BW_PATH` as an environment variables as a replacement to `apppath`

## commands and options table
| command / option | description
|----|-----|
login [username]    | required if user have not initialized bitwarden-cli
sync                | syncs local bitwarden vault
unlock              | unlocks the vault to obtain session
savejson            | export userdata
export              | export attachments
--dump              | will also export the appdata that contains more sensitive information
autoe               | all-in-one press to go
--

# example
## autoe
```
bw-export --pw [password] autoe
```

## login
```
bw-export --pw [password] login [username]
```

## chained
```
bw-export --pw [password] login [username] unlock sync savejson export --dump
```


# required package
click

# Author
Zackary W

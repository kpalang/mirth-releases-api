# Mirth Resources REST API
A REST API for providing programmatic access to Mirth resources.

## Overview

So basically this project helps whoever's interested with programmatic parsing/download of [Mirth Connect](https://github.com/nextgenhealthcare/connect/) releases.

Every midnight, an action checks for new releases. If found, it's metadata is added to [`releases.json`](https://github.com/kpalang/mirth-releases-api/blob/master/releases.json) and [`releases.min.json`](https://github.com/kpalang/mirth-releases-api/blob/master/releases.min.json) files with the following structure:

```json
{
    "os": "windows",
    "arch": "x86",
    "downloadType": "installer",
    "downloadUrl": "https://s3.amazonaws.com/downloads.mirthcorp.com/connect/4.2.0.b2825/mirthconnect-4.2.0.b2825-windows-x32.exe",
    "sha256": "6769801a9b76045a25ca927f67e7f5897f18ba2c12e66a7c2ffae63d430f8bb6",
    "md5": "0687cddd5815ffeb973e0a7ef8e716e7",
    "publishedAt": "2022-12-07T18:43:04Z",
    "tagName": "4.2.0"
}
```

## Usage
Download yourselves either the beautified [`releases.json`](https://raw.githubusercontent.com/kpalang/mirth-releases-api/master/releases.json) or minified [`releases.min.json`](https://raw.githubusercontent.com/kpalang/mirth-releases-api/master/releases.min.json) and parse it as you wish.

### Example 1
```sh
cat releases.min.json | jq -r '.[] | select(.os=="windows" and .arch=="x64" and .tagName=="3.6.0" and .downloadType=="zip")' 
```
```json
{
  "os": "windows",
  "arch": "x64",
  "downloadType": "zip",
  "downloadUrl": "https://s3.amazonaws.com/downloads.mirthcorp.com/connect/3.6.0.b2287/mirthconnect-3.6.0.b2287-windows-x64.zip",
  "sha256": "a9a4cd77db6ddc71237f944e82d1be0acd7a99f20ec45f2ce347087f193b8e4e",
  "md5": "fafa8e004a427d90d9905e61afdb2008",
  "publishedAt": "2018-06-07T16:15:09Z",
  "tagName": "3.6.0"
}
```

### Example 2
```sh
cat releases.min.json | jq -r '.[] | select(.os=="linux" and .arch=="x64" and .tagName=="4.2.0" and .downloadType=="tar.gz")'
```
```json
{
  "os": "linux",
  "arch": "x64",
  "downloadType": "tar.gz",
  "downloadUrl": "https://s3.amazonaws.com/downloads.mirthcorp.com/connect/4.2.0.b2825/mirthconnect-4.2.0.b2825-unix.tar.gz",
  "sha256": "9ab928069ec263edf76b168739e5091cbd864971c2af1be05a845d19660fd7a0",
  "md5": "4f3c0e5eaeed724d4e740de94d8636ee",
  "publishedAt": "2022-12-07T18:43:04Z",
  "tagName": "4.2.0"
}
```

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

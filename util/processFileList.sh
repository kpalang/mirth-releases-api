#!/bin/bash

runner_index=$1
repository_url=$2
version=$3
server_id=$4

while IFS="" read -r line || [ -n "$line" ]; do
  group_id=$(cut -d':' -f1 <<<"$line")
  path=$(cut -d':' -f2 <<<"$line")
  filename=$(basename "$path")
  artifact_id=${filename%.*}

  mvn deploy:deploy-file \
    -Dfile="$path" \
    -Dpackaging=jar \
    -DrepositoryId="$server_id" \
    -DartifactId="$artifact_id" \
    -DgroupId="$group_id" \
    -Dversion="$version" \
    -Durl="$repository_url"
done <artifact-list-split.txt."$runner_index"

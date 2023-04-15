#!/bin/bash

mirth_root="$(pwd)/mirthconnect"
output_file="artifact-list-complete.txt"
artifact_index_path='util/artifactIndex.json'

jq --compact-output -r '.[]' $artifact_index_path |
while IFS= read -r artifactData; do
  groupId=$(echo "$artifactData" | jq -r '.groupId')
  path=$(echo "$artifactData" | jq -r '.path')

  abs_path="$mirth_root/$path"

  if [[ -d $abs_path ]]; then
    # Get *.jar in child directory
    find "$abs_path" -type f -name '*.jar' | while read file; do
      echo "$groupId":"$file" >> $output_file
    done
  elif [[ -f $abs_path ]]; then
    echo "$groupId":"$abs_path" >> $output_file
  else
    echo "$abs_path is not valid"
    exit 1
  fi
done

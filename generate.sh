#!/bin/bash

cd lessons || exit 1

for dir in */; do
  echo "Processing $dir"
  cd "$dir" || continue

  shopt -s nullglob
  for mdfile in *.md; do
    echo " - Generating HTML and PPTX for $mdfile"
    base="${mdfile%.md}"
    npx @marp-team/marp-cli@latest "$mdfile" -o "${base}.html" --theme ../../theme.css
    npx @marp-team/marp-cli@latest "$mdfile" -o "${base}.pptx" --theme ../../theme.css --allow-local-files
  done
  shopt -u nullglob

  cd ..
done

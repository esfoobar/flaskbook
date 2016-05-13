#!/bin/sh

# Convert steps(branches) to modules(tags) using a max # of steps

max=1
for i in `seq 20 $max`
do
    echo "Tagging step $i"
    git checkout step-${i}
    git tag module-${i}
    git checkout master
    git branch step-${i} -d
    git push origin :step-${i}
done
git push origin --tags
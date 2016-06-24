file="$1"
javac "$file"
java "${file%.*}"

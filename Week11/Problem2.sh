read -p "Enter a number to calculate its factorial: " num

factorial=1

if [ $num -lt 0]
then 
        echo "Factorial of a negative number does not exist."
        exit 1
fi

for (( i=1; i<=num; i++ ))
do
    factorial=$((factorial*i))
done

echo "The factorial of $num is $factorial."

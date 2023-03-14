#!/usr/bin/node
let number = process.argv[2]

number = parseInt(number);

if (isNaN(process.argv[2]) || number === 1)
{
	number = 0
}


for (let i = 3; i < process.argv.length; i++)
{
	let compare = parseInt(process.argv[i]);

	if (number < compare)
	{
		number = compare
	}
}
console.log(number)

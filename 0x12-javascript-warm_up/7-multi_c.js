#!/usr/bin/node
let num = process.argv[2];
const myVar = '“C is fun”';
if (num)
{
	for (let i = 0; i < num; i++)
	{
  	console.log(myVar);
	}
}
else if (!num)
{
  	console.log("Missing number of occurrences");
}

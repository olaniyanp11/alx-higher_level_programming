#!/usr/bin/node

let num = process.argv[2];
for (let i = 0; i < num; i++)
{
	for (let j = 0; j < num; j++)
	{
		process.stdout.write("x");
	}
		process.stdout.write("\n");
}

#!/usr/bin/node
function add(a, b)
{
	console.log(a + b);
}

a = Number(process.argv[2]);
b = Number(process.argv[3]);
add(a, b);

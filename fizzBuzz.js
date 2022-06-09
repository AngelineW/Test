    let x = 1;

    while ( x <= 100)
    {
        if (x % 3 === 0 && x % 5 === 0) // start with this condition, otherwise julia or james will be given priority.
            console.log("juliajames");

        else if (x % 3 === 0)
            console.log( "julia");

        else if (x % 5 === 0)
            console.log("james");

        else {
            console.log(x);
        }

        x++;
    }

    
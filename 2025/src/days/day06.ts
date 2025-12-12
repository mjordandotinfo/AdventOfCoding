export function part1(lines: string[]) {
    const line1: number[] = lines[0].trim().split(/\s+/).map((value) => +value);
    const line2: number[] = lines[1].trim().split(/\s+/).map((value) => +value);
    const line3: number[] = lines[2].trim().split(/\s+/).map((value) => +value);
    const line4: number[] = lines[3].trim().split(/\s+/).map((value) => +value);
    const operators: string[] = lines[4].trim().split(/\s+/);

    console.log([line1.length, line2.length, line3.length, operators.length]);
    let total = 0;
    for (let i = 0; i < line1.length; i += 1) {
        let subtotal = 0;
        if (operators[i] == "+") {
            subtotal = (line1[i] + line2[i] + line3[i] + line4[i]);
        }
        
        if (operators[i] == "*") {
            subtotal = (line1[i] * line2[i] * line3[i] * line4[i]);
        } 

        console.log([line1[i], line2[i], line3[i], subtotal]);
        total += subtotal;
    }

    return total;
}


export function part2(lines: string[]) {

    const numbers: string[] = [];
    const operands: string = lines[lines.length-1];
    
    for (let i = 0; i < lines.length - 1; i += 1) {
        numbers.push(lines[i]);
    }

    let total = 0;
    for (let i = 0; i < numbers[0].length; i += 4) {
        let currentNumbers = numbers.map((num) => {
            return num.slice(i, i+3)
        });

        // console.log(currentNumbers);

        const transposedNumbers = Array.from({length: 3}, (_, i) => currentNumbers.map((num) => num[i]).join(''));
        console.log(transposedNumbers);

        let subtotal = 0;
        if (operands[i] == "+") {
            transposedNumbers.forEach((num) => {
                subtotal += Number(num);
            })
            console.log(subtotal)
        }

        if (operands[i] == "*") {
            subtotal = 1;
            transposedNumbers.forEach((num) => {
                subtotal *= Number(num);
            })
            console.log(subtotal)
        }

        total += subtotal;
    //     let num1 = numbers[0].slice(i, i+3);
    //     console.log(num1);
    }

    return total;
}
// function parseInputs(lines: string[]){
//     return lines[0].split(',').map(range => { 
//         return range.split('-').map(num => +num)
//     });
// }

export function part1(lines: string[]){
    let sum = 0;
    lines.forEach((line) => {
        const bank = `${line}`
        let digitOne = bank[0];
        let digitTwo = bank[1];
        // search through each of the digits 
        for (let i = 1; i < bank.length - 1; i++) {
            if (bank[i] > digitOne) {
                digitOne = bank[i];
                digitTwo = bank[i+1];
            } else if (bank[i] > digitTwo) {
                digitTwo = bank[i];
            }
        }

        // chec last digit
        if (bank[bank.length - 1] > digitTwo) {
            digitTwo = bank[bank.length - 1];
        }

        const jolts = Number(digitOne + digitTwo);
        sum += jolts;
        // console.log(jolts);
        
    });

    // console.log(sum);

    return sum;
}

export function part2(lines: string[]){
// bucket indices by digit value
    class Jolt {
        constructor(
            public value = '-1',
            public index = -1
        ) {}
    }


    [[0], [0], [0,]]
  // find first index that the number is great than and put it there

    let sum = 0;
    lines.forEach((line) => {
    // const line = lines[1];
        const bank = `${line}`
        const jolts = Array.from({length: 12}, () => new Jolt);
        let lockedIn = 0;
        // console.log(jolts);

        for (let bankIndex = 0; bankIndex < bank.length; bankIndex++){
            const currentJolt = new Jolt(bank[bankIndex], bankIndex);
            // console.log(currentJolt);

            if (bank.length - bankIndex + 1 <= jolts.length){
                lockedIn += 1;
                // console.log(`${bankIndex} - ${lockedIn}`);
            }

            for (let joltIndex = lockedIn; joltIndex < jolts.length; joltIndex++) {
                if (currentJolt.value > jolts[joltIndex].value && currentJolt.index > jolts[joltIndex].index) {
                    jolts[joltIndex].value = currentJolt.value;
                    jolts[joltIndex].index = currentJolt.index;
                    // console.log("True");
                    break;
                }
            }

            // console.log(jolts);
        }


        const result = jolts.map(jolt => jolt.value).join("");
        // console.log(result);
        sum += Number(result);
    });

    console.log(sum);

    return sum;
}
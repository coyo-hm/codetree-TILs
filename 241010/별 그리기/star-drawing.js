const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim()
const n = Number(input);
let ans = ""

for(let i = 1; i <= n; i++){
    ans = " ".repeat(n - i) + "*".repeat(2 * i - 1)
    console.log(ans)
}

for(let i = 1; i < n; i++){
    ans = " ".repeat(i) + "*".repeat(2 * (n - i) - 1)
    console.log(ans)
}
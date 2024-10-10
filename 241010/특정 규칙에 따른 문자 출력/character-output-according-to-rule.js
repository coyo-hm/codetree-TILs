const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim()
const n = Number(input)
let ans = ""

for(let i = 0; i < n; i++){
    ans = " ".repeat((n - i - 1) * 2)
    ans += "@".repeat(i + 1).split("").join(" ")
    console.log(ans)
}

for(let i = n - 1; i > 0; i--){
    ans = "@".repeat(i).split("").join(" ")
    console.log(ans)
}
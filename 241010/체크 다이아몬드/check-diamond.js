const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();
const n = Number(input);
let ans = ""

for(let i = 1; i <= n; i++){
    ans = " ".repeat(n - i)
    ans += "* ".repeat(i).trim()
    console.log(ans)
}

for(let i = n - 1; i > 0; i--){
    ans = " ".repeat(n - i)
    ans += "* ".repeat(i).trimEnd()
    console.log(ans)
}
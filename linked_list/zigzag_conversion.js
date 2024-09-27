/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    // If numRows is 1, there's no zigzag pattern, return the string as it is.
    if (numRows === 1) return s;

    // Create an array of strings to store the characters for each row.
    let rows = new Array(Math.min(numRows, s.length)).fill("");

    // Variables to track the current row and direction.
    let curRow = 0;
    let goingDown = false;

    // Traverse the string and place characters into the correct rows.
    for (let c of s) {
        rows[curRow] += c;
        if (curRow === 0 || curRow === numRows - 1) goingDown = !goingDown;
        curRow += goingDown ? 1 : -1;
    }

    // Join all the rows to form the final zigzag string.
    return rows.join("");
};

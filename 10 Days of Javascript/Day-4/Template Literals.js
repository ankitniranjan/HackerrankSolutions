/*
 * Determine the original side lengths and return an array:
 * - The first element is the length of the shorter side
 * - The second element is the length of the longer side
 * 
 * Parameter(s):
 * literals: The tagged template literal's array of strings.
 * expressions: The tagged template literal's array of expression values (i.e., [area, perimeter]).
 */
 
function sides(literals, ...expressions) {
    let A = expressions[0];
    let P = expressions[1];
    
    let s1 = (P + Math.sqrt(P*P - 16*A)) / 4;
    let s2 = (P - Math.sqrt(P*P - 16*A)) / 4;
    
    const result = [s1,s2];
    return result.sort();
}


function main() {
    let s1 = +(readLine());
    let s2 = +(readLine());
    
    [s1, s2] = [s1, s2].sort();
    
    const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;
    
    console.log((s1 === x) ? s1 : -1);
    console.log((s2 === y) ? s2 : -1);
}

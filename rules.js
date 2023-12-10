let instructions;

function closeRules() {
    let modal = document.getElementById("modal");
    let overlay = document.getElementById("overlay");
    modal.classList.remove("isVisible");
    overlay.classList.remove("isVisible");
}
 
function openRules() {
    let modal = document.getElementById("modal");
    let overlay = document.getElementById("overlay");
    modal.classList.add("isVisible");
    overlay.classList.add("isVisible");
}
 
closeRules();
 
/*
 
RULES
 
Pig out: lose all turn points; next turn
Sider: 1 point
 
Trotter: 5 points
Double Trotter: 20 points  (or 4x)
 
Razorback: 5 points
Double Razorback: 20 points  (or 4x)
 
Snouter: 10pts
Double snouter: 40pts  (or 4x)
 
leaning jowler: 15pts
double leaning jowler: 60 points (or 4x)
 
mixed combo: add single points (unless mixed with sider; then sider is 0)
 
Oinker (touching pigs): lose all game points; next turn
 */
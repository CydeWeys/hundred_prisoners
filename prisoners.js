//!/usr/bin/node


// These are your input parameters. The default values are sane, though feel
// free to adjust to play around. n = 3 makes for a good base case.
var n = 100; // The number of prisoners
var ratio = 0.5; // The probability that a prisoner's value is True

//
// This is the function you need to implement.
//
// i is the number of this prisoner, from 0 to n-1.
// dead is a list of booleans for whether or not each previous prisoner died.
// declared is a list of booleans that each previous prisoner declared.
//     For both of these lists, the result of the most recent prisoner to go is
//     the last element, and these lists are both empty for the first prisoner to go.
// ahead is a list of booleans for all prisoners that the current prisoner can see.
//     For this list, the next prisoner to go is the first element, and the last
//     prisoner to go will have an empty ahead list.
// Returns: The boolean that the current prisoner declares.
function prisonerAction(i, dead, declared, ahead) {
  // Your implementation goes here. All prisoners declaring themselves True is
  // going to kill a lot of them. Can you do better?
  return true;
}

// Don't change any code beyond this line. This is the bookkeeping of the simulation.
(function run() {
  var prisoners = Array.apply(null, new Array(n)).map(function() { return Math.random() < ratio; });
  var ahead = Array.prototype.concat([], prisoners);
  var dead = [];
  var declared = [];

  // The game loop
  for(var i = 0; i < n; i++) {
    ahead.pop(0);
    var declaration = prisonerAction(i, dead, declared, ahead);
    declared.push(declaration);
    dead.push(declaration !== prisoners[i]);
  }

  var numDead = dead.filter(Boolean).length;
  console.log('Out of %d prisoners, you killed %d.', n, numDead);
  if (numDead > 1 || dead.slice(1).filter(Boolean).length) {
    console.log('You can do better than that!');
  } else {
    console.log('Great job! You found the right algorithm!');
  }
})();

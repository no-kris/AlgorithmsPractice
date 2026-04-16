// Implementation for energy_balancer.md problem

// Sliding window O(n)
//
export function energy_balancer(powerOutputs, range, limit) {
  if (powerOutputs.length == 0 || range > powerOutputs.length) {
    return false;
  }

  let currentSum = 0;
  for (let i = 0; i < range; i++) {
    currentSum += powerOutputs[i];
  }

  if (currentSum > limit) {
    return false;
  }

  for (let i = range; i < powerOutputs.length; i++) {
    // currentSum becomes the currentSum minus the value leaving the range
    // plus the new value entering the range
    currentSum = currentSum - powerOutputs[i - range] + powerOutputs[i];
    if (currentSum > limit) {
      return false;
    }
  }

  return true;
}

// Brute force sliding window O(n * k)
//
// export function energy_balancer(powerOutputs, range, limit) {
//   if (powerOutputs.length === 0 || range > powerOutputs.length) {
//     return false;
//   }

//   for (let outer = 0; outer <= powerOutputs.length - range; outer++) {
//     let currentSum = 0;
//     for (let inner = outer; inner < outer + range; inner++) {
//       currentSum += powerOutputs[inner];
//     }
//     if (currentSum > limit) {
//       return false;
//     }
//   }
//   return true;
// }

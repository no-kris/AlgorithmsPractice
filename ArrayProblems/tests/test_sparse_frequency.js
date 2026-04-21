const assert = require("assert");
const { sparseFreq } = require("../sparse_frequency");

function testSparseFreq() {
  // Example 1
  const res1 = sparseFreq([10, 20, 10, 30, 10, 20, 30, 30, 30]);
  assert.deepStrictEqual(res1, { 10: 3, 20: 2 });

  // Example 2
  const res2 = sparseFreq([5, 5, 5, 5, 5]);
  assert.deepStrictEqual(res2, { 5: 5 });

  // Example 3
  const res3 = sparseFreq([1, 2, 3, 4]);
  assert.deepStrictEqual(res3, {});

  // Edge case: Frequency of 1 (not prime)
  const res4 = sparseFreq([7, 7, 8]);
  assert.deepStrictEqual(res4, { 7: 2 });

  console.log("All tests passed!");
}

testSparseFreq();

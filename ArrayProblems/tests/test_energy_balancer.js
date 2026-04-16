import { energy_balancer } from "../energy_balancer.js";
import assert from "assert";

function runTests() {
  // Example 1
  assert.strictEqual(
    energy_balancer([1, 2, 3, 4], 2, 5),
    false,
    "Example 1 failed",
  );

  // Example 2
  assert.strictEqual(
    energy_balancer([1, 2, 3, 4], 2, 7),
    true,
    "Example 2 failed",
  );

  // Example 3
  assert.strictEqual(
    energy_balancer([5, 5, 5], 1, 4),
    false,
    "Example 3 failed",
  );

  // Additional cases
  // Edge case: k = array length
  assert.strictEqual(
    energy_balancer([1, 2, 3], 3, 6),
    true,
    "Edge case k=length failed",
  );
  assert.strictEqual(
    energy_balancer([1, 2, 3], 3, 5),
    false,
    "Edge case k=length failed",
  );

  // Single element
  assert.strictEqual(
    energy_balancer([5], 1, 5),
    true,
    "Single element success",
  );
  assert.strictEqual(
    energy_balancer([5], 1, 4),
    false,
    "Single element failure",
  );

  console.log("All tests passed!");
}

runTests();

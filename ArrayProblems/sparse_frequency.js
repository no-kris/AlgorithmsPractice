// Implementation for sparse_frequency.md problem using JavaScript

const isPrime = (num) => {
  if (num < 2) {
    return false;
  }
  for (let i = 2; i < num; i++) {
    if (num % i == 0) return false;
  }
  return true;
};

export function sparseFreq(pings) {
  let primes = {};
  let pingCounts = {};
  for (const ping of pings) {
    pingCounts[ping] = (pingCounts[ping] || 0) + 1;
  }
  for (const [key, value] of Object.entries(pingCounts)) {
    if (isPrime(value)) {
      primes[key] = value;
    }
  }
  return primes;
}

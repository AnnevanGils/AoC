#include <cassert>
#include <chrono>
#include <fstream>
#include <iostream>
#include <math.h>
#include <vector>

long glue_digits_together(std::vector<int> &digits) {
  long n = 0;
  int power = 0;
  for (auto it = digits.rbegin(); it != digits.rend(); ++it) {
    int d = *it;
    n += d * std::pow(10, power);
    power++;
  }
  return n;
}

long get_max_joltage(std::string &bank, int n) {
  std::vector<int> digits(n);
  int j_start = 0;
  for (int i = 0; i < n; i++) {
    int max_digit = 0;
    int j_cap = bank.size() - (n - 1) + i;
    for (int j = j_start; j < j_cap; j++) {
      int d = bank[j] - '0';
      if (d > max_digit) {
        max_digit = d;
        j_start = j + 1;
      }
    }
    digits[i] = max_digit;
  }
  return glue_digits_together(digits);
}

int main() {
  // Load input file (this file is copied to the build directory)
  std::fstream infs("input.txt");
  if (!infs.is_open()) {
    std::cerr << "Failed to open file\n";
    return 1;
  }

  auto start = std::chrono::steady_clock::now();

  long part1 = 0;
  long long part2 = 0;
  std::string line;
  while (std::getline(infs, line)) {
    part1 += get_max_joltage(line, 2);
    part2 += get_max_joltage(line, 12);
  }

  auto end = std::chrono::steady_clock::now();
  std::chrono::duration<double> elapsed = end - start;
  std::cout << "Elapsed time: " << elapsed.count() << " seconds\n";

  std::cout << std::endl;
  std::cout << "part1: " << part1 << std::endl;
  std::cout << "part2: " << part2 << std::endl;

  return 0;
}

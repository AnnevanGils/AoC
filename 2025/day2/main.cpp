#include <algorithm>
#include <cassert>
#include <chrono>
#include <fstream>
#include <iostream>
#include <vector>

bool check_invalid(std::string &left, std::string &right,
                   int start_idx_left = 0, int start_idx_right = 0) {
  if (left.substr(start_idx_left)[0] != right.substr(start_idx_right)[0]) {
    return false;
  }
  if (start_idx_left == left.size() - 1) {
    return left == right;
  }
  return check_invalid(left, right, start_idx_left + 1, start_idx_right + 1);
}

bool check_valid(std::string &id) {
  if (id.size() % 2 != 0) {
    return true;
  }
  int size = id.size();
  std::string left = id.substr(0, size / 2);
  std::string right = id.substr(size / 2);

  assert(left.size() == right.size());

  return !check_invalid(left, right);
}

bool check_invalid_p2(std::string &id) {
  for (int i = 2; i <= id.size(); i++) {
    if (id.size() % i != 0) {
      continue;
    }
    int interval = id.size() / i;
    std::vector<int> parts;
    int compare_to_nr = -1;
    for (int j = 0; j < i; j++) {
      int nr = std::stoi(id.substr(j * interval, interval));
      if (compare_to_nr == -1) {
        compare_to_nr = nr;
      }
      parts.push_back(nr);
      if (compare_to_nr != nr) {
        goto next_outer;
      }
    }

    // returns invalid true
    return true;

  next_outer:
    continue;
  }
  // return invalid false
  return false;
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
  long part2 = 0;
  std::string line;
  while (std::getline(infs, line, ',')) {
    int pos = line.find('-', 0);
    std::string low = line.substr(0, pos);
    std::string high = line.substr(pos + 1);
    long low_int = std::stol(low);
    long high_int = std::stol(high);
    for (long i = low_int; i <= high_int; i++) {
      std::string id_str = std::to_string(i);
      if (!check_valid(id_str)) {
        part1 += i;
      };
      if (check_invalid_p2(id_str)) {
        part2 += i;
      };
    }
  }

  auto end = std::chrono::steady_clock::now();
  std::chrono::duration<double> elapsed = end - start;
  std::cout << "Elapsed time: " << elapsed.count() << " seconds\n";

  std::cout << std::endl;
  std::cout << "part1: " << part1 << std::endl;
  std::cout << "part2: " << part2 << std::endl;

  return 0;
}

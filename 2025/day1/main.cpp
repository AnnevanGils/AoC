#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

// returns {new pointer value, nr of clicks by rotating}
// a click is a pass through 0 or ending at 0
std::tuple<int, int> rotate(int current_point, int rotation) {
  int clicks = abs(rotation / 100);
  rotation = rotation % 100;

  clicks += (current_point + rotation) / 100;

  int mod_value = (current_point + rotation) % 100;

  if (mod_value < 0 && current_point > 0) {
    clicks++;
  }

  if (mod_value == 0 && rotation < 0) {
    clicks++;
  }

  int new_pointer_value = (mod_value < 0) ? 100 + mod_value : mod_value;

  return {new_pointer_value, clicks};
}

int main() {
  // Load input file (this file is copied to the build directory)
  std::fstream infs("input.txt");
  if (!infs.is_open()) {
    std::cerr << "Failed to open file\n";
    return 1;
  }

  int part1 = 0;
  int current_point = 50;
  int part2 = 0;
  std::string line;
  while (std::getline(infs, line)) {
    int rot = std::stoi(line.substr(1));
    int direction = line[0] == 'L' ? -1 : 1;

    auto [new_current_point, clicks] = rotate(current_point, direction * rot);

    std::cout << line << " " << new_current_point << " " << clicks << std::endl;

    current_point = new_current_point;
    if (current_point == 0) {
      part1++;
    }
    part2 += clicks;
  }

  std::cout << std::endl << "part 1: " << part1 << std::endl;
  std::cout << std::endl << "part 2: " << part2 << std::endl;

  return 0;
}
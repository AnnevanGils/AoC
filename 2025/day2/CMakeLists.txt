# Get the last component of the current source dir
get_filename_component(TARGET_NAME ${CMAKE_CURRENT_SOURCE_DIR} NAME)

# Create executable with that name
add_executable(${TARGET_NAME} main.cpp)

configure_file(input.txt input.txt)
configure_file(test_input.txt test_input.txt)

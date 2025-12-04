#!/bin/bash
# $1 = source folder (e.g., 2025/day1)
# $2 = build folder root (e.g., build)

SRC="$1"
BUILD_ROOT="$2"

TARGET_NAME=$(basename "$SRC")
BUILD_DIR="$BUILD_ROOT/$TARGET_NAME"

cmake -S "$SRC" -B "$BUILD_DIR"
cmake --build "$BUILD_DIR"
cd $BUILD_DIR
"./$TARGET_NAME"

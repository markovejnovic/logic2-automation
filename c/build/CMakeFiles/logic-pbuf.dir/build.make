# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/marko/Desktop/logic2-automation/c

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/marko/Desktop/logic2-automation/c/build

# Utility rule file for logic-pbuf.

# Include any custom commands dependencies for this target.
include CMakeFiles/logic-pbuf.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/logic-pbuf.dir/progress.make

CMakeFiles/logic-pbuf: SOURCE
CMakeFiles/logic-pbuf: /home/marko/Desktop/logic2-automation/proto
	protoc --c_out=/home/marko/Desktop/logic2-automation/c/build/codegen/proto -I /home/marko/Desktop/logic2-automation/c/../proto /home/marko/Desktop/logic2-automation/c/../proto/saleae/grpc/saleae.proto

logic-pbuf: CMakeFiles/logic-pbuf
logic-pbuf: CMakeFiles/logic-pbuf.dir/build.make
.PHONY : logic-pbuf

# Rule to build all files generated by this target.
CMakeFiles/logic-pbuf.dir/build: logic-pbuf
.PHONY : CMakeFiles/logic-pbuf.dir/build

CMakeFiles/logic-pbuf.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/logic-pbuf.dir/cmake_clean.cmake
.PHONY : CMakeFiles/logic-pbuf.dir/clean

CMakeFiles/logic-pbuf.dir/depend:
	cd /home/marko/Desktop/logic2-automation/c/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/marko/Desktop/logic2-automation/c /home/marko/Desktop/logic2-automation/c /home/marko/Desktop/logic2-automation/c/build /home/marko/Desktop/logic2-automation/c/build /home/marko/Desktop/logic2-automation/c/build/CMakeFiles/logic-pbuf.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/logic-pbuf.dir/depend


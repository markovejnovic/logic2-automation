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

# Include any dependencies generated for this target.
include CMakeFiles/libsaleae.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/libsaleae.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/libsaleae.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/libsaleae.dir/flags.make

CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.o: CMakeFiles/libsaleae.dir/flags.make
CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.o: /home/marko/Desktop/logic2-automation/c/src/saleae/automation/manager.c
CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.o: CMakeFiles/libsaleae.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/marko/Desktop/logic2-automation/c/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.o"
	/usr/lib64/ccache/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.o -MF CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.o.d -o CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.o -c /home/marko/Desktop/logic2-automation/c/src/saleae/automation/manager.c

CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.i"
	/usr/lib64/ccache/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/marko/Desktop/logic2-automation/c/src/saleae/automation/manager.c > CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.i

CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.s"
	/usr/lib64/ccache/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/marko/Desktop/logic2-automation/c/src/saleae/automation/manager.c -o CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.s

# Object files for target libsaleae
libsaleae_OBJECTS = \
"CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.o"

# External object files for target libsaleae
libsaleae_EXTERNAL_OBJECTS =

liblibsaleae.a: CMakeFiles/libsaleae.dir/src/saleae/automation/manager.c.o
liblibsaleae.a: CMakeFiles/libsaleae.dir/build.make
liblibsaleae.a: CMakeFiles/libsaleae.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/marko/Desktop/logic2-automation/c/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C static library liblibsaleae.a"
	$(CMAKE_COMMAND) -P CMakeFiles/libsaleae.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/libsaleae.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/libsaleae.dir/build: liblibsaleae.a
.PHONY : CMakeFiles/libsaleae.dir/build

CMakeFiles/libsaleae.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/libsaleae.dir/cmake_clean.cmake
.PHONY : CMakeFiles/libsaleae.dir/clean

CMakeFiles/libsaleae.dir/depend:
	cd /home/marko/Desktop/logic2-automation/c/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/marko/Desktop/logic2-automation/c /home/marko/Desktop/logic2-automation/c /home/marko/Desktop/logic2-automation/c/build /home/marko/Desktop/logic2-automation/c/build /home/marko/Desktop/logic2-automation/c/build/CMakeFiles/libsaleae.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/libsaleae.dir/depend


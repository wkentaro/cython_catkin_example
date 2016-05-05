cmake_minimum_required(VERSION 2.8.3)
project(cython_catkin_example)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES cython_catkin_example
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

###########
## Build ##
###########

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake)
include(UseCython)
add_subdirectory(python/${PROJECT_NAME})


#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
  catkin_add_nosetests(python/${PROJECT_NAME}/tests)
endif()

cmake_minimum_required(VERSION 3.1...3.27)

project(
    libsaleae
    VERSION 0.1
    LANGUAGES C)

add_custom_target(proto-directory
    COMMAND ${CMAKE_COMMAND} -E make_directory
    ${CMAKE_CURRENT_BINARY_DIR}/codegen/proto
)
add_custom_target(logic-pbuf
    COMMAND protoc
        --c_out=${CMAKE_CURRENT_BINARY_DIR}/codegen/proto
        -I ${CMAKE_SOURCE_DIR}/../proto
        ${CMAKE_SOURCE_DIR}/../proto/saleae/grpc/saleae.proto
    DEPENDS proto-directory
    SOURCE ${CMAKE_SOURCE_DIR}/../proto
)

add_library(
    libsaleae
    src/saleae/automation/manager.c
)
target_include_directories(libsaleae
                           PUBLIC include
                           PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/codegen
                           DEPENDS logic-pbuf)

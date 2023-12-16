#ifndef SALEAE_AUTOMATION_MANAGER_H
#define SALEAE_AUTOMATION_MANAGER_H

#include <stdint.h>

/// @brief Encodes a semver version code.
typedef struct {
    unsigned int major;
    unsigned int minor;
    unsigned int patch;
} logic2_api_version;

/// @brief Encodes the logic 2 application information structure.
typedef struct {
    logic2_api_version api_version; /*!< saleae.proto version server is on */
    char* app_version; /*!< Logic 2 app version */
    int app_pid; /*!< Application process ID */
} logic2_appinfo;

/// @brief Represents the Saleae Logic2 Manager API.
typedef struct saleae_manager_s* saleae_manager;

/// @brief Represents the saleae device.
///
/// @todo Unlike the python API, the C API does not import the saleae-pb-c.h
///       file. The reason I chose to avoid doing that is because I want to
///       avoid exposing The saleae.pb-c.h file to public consumers of this
///       interface.
typedef enum {
    SALEAE_DEVICE_UNSPECIFIED,
    SALEAE_DEVICE_LOGIC,
    SALEAE_DEVICE_LOGIC_4,
    SALEAE_DEVICE_LOGIC_8,
    SALEAE_DEVICE_LOGIC_16,
    SALEAE_DEVICE_LOGIC_PRO_8,
    SALEAE_DEVICE_LOGIC_PRO_16,
} saleae_device_type;

saleae_manager saleae_manager_connect(
    const char* address,
    uint16_t port,
    unsigned long connect_timeout_ms
);

saleae_manager saleae_manager_launch(
    const char* application_path,
    uint16_t port,
    unsigned long connect_timeout_ms
);

/// @return The connected application infromation or `NULL` if no Logic2 is
/// connected.
const logic2_appinfo* saleae_manager_get_appinfo(saleae_manager manager);

void saleae_manager_destroy(saleae_manager);

#endif // SALEAE_AUTOMATION_MANAGER_H

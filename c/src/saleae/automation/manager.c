#include "saleae/automation/manager.h"
#include "proto/saleae/grpc/saleae.pb-c.h"
#include <stdlib.h>

// TODO: Cross-platform support.
#include <unistd.h>
#include <stdio.h>
static pid_t launch_logic(const char* path_to_binary, uint16_t port) {
    char port_str[6]; // 6 bytes corresponds to XXXXX\0
    snprintf(port_str, sizeof(port_str), "%d", port);

    pid_t pid = fork();
    if (pid == 0) {
        execl(path_to_binary, "--automation", "--automationPort", port_str);
    }

    return pid;
}
// END TODO

struct saleae_manager_s {
    pid_t logic_pid;
    logic2_appinfo appinfo;
};

saleae_manager saleae_manager_launch(
    const char *application_path,
    uint16_t port,
    unsigned long connect_timeout_ms
) {
    saleae_manager manager = malloc(sizeof(struct saleae_manager_s));
    manager->logic_pid = launch_logic(application_path, port);
    if (manager->logic_pid == -1) {
        // TODO: Error case
    }
}

const logic2_appinfo* saleae_manager_get_appinfo(saleae_manager manager) {
    const Saleae__Automation__GetAppInfoRequest request =
        SALEAE__AUTOMATION__GET_APP_INFO_REQUEST__INIT;

}

#ifndef SALEAE_AUTOMATION_ERRORS_HPP
#define SALEAE_AUTOMATION_ERRORS_HPP

#include <stdexcept>
#include <string_view>

namespace saleae {
namespace automation {

/// @brief The base class for all Saleae exceptions. Do not catch this directly.
struct SaleaeError : public std::runtime_error {
    SaleaeError(std::string_view message) : std::runtime_error(message) {}
};

/// @brief This indicates that the error message from the Logic 2 software was not understood by the python library.
/// @note This could indicate a version mismatch.
struct UnknownError final : public SaleaeError {
    UnknownError(std::string_view message) : SaleaeError(message) {}
};

/// @brief This indicates that there was an instance of Logic 2 already running.
struct Logic2AlreadyRunningError final : public SaleaeError {
    Logic2AlreadyRunningError(std::string_view message) : SaleaeError(message) {}
};

/// @brief This indicates that the server is running an incompatible API
///        version. This only happens on major version changes. It is
///        recommended to upgrade to the latest release of Logic 2 and the
///        C++ API.
struct IncompatibleApiVersionError final : public SaleaeError {
    IncompatibleApiVersionError(std::string_view message) : SaleaeError(message) {}
};

/// @brief An unexpected error occurred in the Logic 2 software. Please submit
/// these errors to Saleae support.
struct InternalServerError final : public SaleaeError {
    InternalServerError(std::string_view message) : SaleaeError(message) {}
};

/// @brief The socket request was invalid. See exception message for details.
struct InvalidRequestError final : public SaleaeError {
    InvalidRequestError(std::string_view message) : SaleaeError(message) {}
};

/// @brief Error loading a saved capture.
/// This could indicate that the file does not exist, or the file was saved
/// with a newer version of the Logic 2 software, or that the file was not a
/// valid saved file. Try manually loading the file in the Logic 2 software for
/// more information.
struct LoadCaptureFailedError final : public SaleaeError {
    LoadCaptureFailedError(std::string_view message) : SaleaeError(message) {}
};

/// @brief An error occurred either while exporting raw data, a single protocol
///        analyzer, or the protocol analyzer data table.
/// Check the exception message for more details.
struct ExportError final : public SaleaeError {
    ExportError(std::string_view message) : SaleaeError(message) {}
};

/// @brief The device ID supplied to the start_capture function is not
///        currently attached to the system, or it has not been detected by the
///        software.
///
/// For general support for device not detected errors, see this support
/// article:
/// https://support.saleae.com/troubleshooting/logic-not-detected
struct MissingDeviceError final : public SaleaeError {
    MissingDeviceError(std::string_view message) : SaleaeError(message) {}
};

/// @brief The base class for all capture related errors. We recommend all
///        automation applications handle this exception type.
///
/// Capture failures occur rarely, and for a handful of reasons. We recommend
/// logging the exception message for later troubleshooting.
///
/// We do not recommend attempting to access or save captures that end in an
/// error. Instead, we recommend starting a new capture.

/// Check the exception message for details.
struct CaptureError : public SaleaeError {
    CaptureError(std::string_view message) : SaleaeError(message) {}
};

/// @brief This error represents any device related error while capturing. USB
/// communication or bandwidth errors, missing calibration, device
/// disconnection while recording, and more.
///
/// Check the exception message for details.
struct DeviceError final : public CaptureError {
    DeviceError(std::string_view message) : CaptureError(message) {}
};

/// @brief This exception indicates that the capture was automatically
///        terminated because the capture buffer was filled.
struct OutOfMemoryError final : public CaptureError {
    OutOfMemoryError(std::string_view message) : CaptureError(message) {}
};

} // namespace automation
} // namespace saleae

#endif // SALEAE_AUTOMATION_ERRORS_HPP
